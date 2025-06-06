<template>
	<Nav/>

	<v-container class="pt-10">
		<v-row justify="center">
			<v-col cols="4" xl="3" class="d-flex justify-center">
				<v-avatar size="300">
					<v-img
						:src="userDetails.profile_picture"
					></v-img>
				</v-avatar>
			</v-col>

			<v-col cols="8" xl="5">
				<v-card>
					<v-card-title>
						<h1>{{ userDetails.username }}
							<v-btn
								v-if="isCurrentProfile"
								icon="mdi-account-edit"
								class="ml-2"
								variant="outlined"
								color="ternary"
								@click="goToEditingView(userId)"
							></v-btn>
						</h1>
					</v-card-title>
					<v-card-subtitle>
						<v-btn
							size="large"
							elevation="0"
							@click="this.$router.push(`/users/${userId}/reviews/all`);"
						>
							<p class="mr-2">{{ score }}</p>

							<p v-for="x in [1, 2, 3, 4, 5]">
								<v-icon v-if="score >= x">
									mdi-star
								</v-icon>
								<v-icon v-else-if="score >= x - 0.5">
									mdi-star-half-full
								</v-icon>
								<v-icon v-else>
									mdi-star-outline
								</v-icon>
							</p>
							
							<p v-if="reviewsCount == 1" class="ml-2">(1 review)</p>
							<p v-else class="ml-2">({{ reviewsCount }} reviews)</p>
						</v-btn>
					</v-card-subtitle>
					<v-spacer class="mb-4"></v-spacer>
					<v-card-subtitle>
						<h2>Joined {{ dateJoined }}</h2>
					</v-card-subtitle>
					<v-card-text>
						<p>{{ userDetails.about }}</p>
					</v-card-text>
				</v-card>
			</v-col>
		</v-row>

		<v-spacer class="my-8"></v-spacer>

		<v-container v-if="isCurrentProfile">
			<v-row>
				<v-col>
					<v-card
						height="120"
						class="d-flex align-center justify-space-between mb-4"
						@click="this.$router.push(`/users/${userDetails.id}/listings`)"
						variant="outlined"
						color="ternary"
						
					>
						<v-card-title>Go to your published listings</v-card-title>

						<v-icon class="mr-4">mdi-arrow-right-bold</v-icon>
					</v-card>

					<v-card
						height="120"
						class="d-flex align-center justify-space-between mb-4"
						variant="outlined"
						color="ternary"
						@click="goToWishlists(userDetails.id)"
					>
						<v-card-title>Go to your wishlists</v-card-title>

						<v-icon class="mr-4">mdi-arrow-right-bold</v-icon>
					</v-card>

					<v-card
						height="120"
						class="d-flex align-center justify-space-between mb-4"
						@click="this.$router.push(`/users/${userDetails.id}/orders`)"
						variant="outlined"
						color="ternary"
						
					>
						<v-card-title>Go to your orders</v-card-title>

						<v-icon class="mr-4">mdi-arrow-right-bold</v-icon>
					</v-card>
				</v-col>
			</v-row>
		</v-container>

		<v-container v-else>
			<v-row>
				<v-col>
					<div class="d-flex justify-space-between">
						<h3>
							Here you can view {{ userDetails.username }}'s featured listings!
						</h3>
						<router-link :to="`/users/${userId}/listings`">
							<v-btn
								append-icon="mdi-arrow-right-bold"
							>
								View all
							</v-btn>
						</router-link>
					</div>
				</v-col>
			</v-row>
			<v-row>
				<v-col
					v-for="listing in featured"
					:cols=4
				>
					<v-hover
						v-slot="{ isHovering, props }"
					>
						<v-img
							:src="listing.photo"
							aspect-ratio="1"
							cover
							v-bind="props"
						>
							<v-expand-transition>
								<div
									v-if="isHovering"
									class="d-flex featured-transition"
								>
									<v-col>
										<v-row class="justify-center text-h4 handwritten">
											<p
												class="wrap-text text-center"
											>
												{{ listing.title }}
											</p>
										</v-row>
										<v-row class="justify-center text-h5">
											<p>{{ listing.price }} €</p>
										</v-row>
										<v-row class="justify-center pa-4">
											<v-btn
												variant="outlined"
												@click="goToListingDetails(listing.id)"
											>
												View details
											</v-btn>
										</v-row>
									</v-col>
								</div>
							</v-expand-transition>
						</v-img>
					</v-hover>
				</v-col>
			</v-row>
		</v-container>
	</v-container>

</template>

<style scoped>
	.featured-transition {
		opacity: .85;
		align-items: center;
		justify-content: center;
		background-color: rgb(var(--v-theme-primary));
		height: 100%;
	}

	.handwritten {
		font-family: 'Homemade Apple', cursive;
	}

	.wrap-text {
		word-wrap: break-word;
		word-break: break-word;
		white-space: normal;
	}
</style>

<script>
	import axios from 'axios';

	export default {
		data() {
			return {
				currentUser: null,
				isCurrentProfile: false,
				userId: this.$route.params.id,
				userDetails: [],
				dateJoined: null,
				score: 0,
				reviewsCount: 0,
				featured: []
			};
		},
		created() {
			this.getCurrentUser();
			this.fetchUserDetails(this.userId);
			this.fetchFeaturedListings(this.userId);
		},
		methods: {
			fetchUserDetails(userId) {
				axios.get(`http://localhost:8000/shop/api/users/${userId}`)
					.then(response => {
						this.userDetails = response.data;
						let options = { year: 'numeric', month: 'long' };
						this.dateJoined = new Date(this.userDetails.date_joined).toLocaleDateString('en-US', options);
						this.score = this.userDetails.avg_score.toFixed(1);
						this.reviewsCount = this.userDetails.no_of_reviews;
						
						this.isCurrentProfile = (this.userDetails.username == this.currentUser.username);
					})
					.catch(error => {
						console.error('Error fetching user details:', error);
					});
			},
			getCurrentUser() {
				axios.get('http://localhost:8000/shop/api/users/current-user')
					.then(response => {
						if (response.data.username) {
							this.currentUser = response.data;
						}
					})
					.catch(error => {
						if (error.response.status != 401) {
							console.error(`Error fetching current user: ${error}`);
						}
					});
			},
			fetchFeaturedListings(userId) {
				axios.get(`http://localhost:8000/shop/api/users/${userId}/featured`)
					.then(response => {
						this.featured = response.data;
					})
					.catch(error => {

					})
			},
			goToEditingView(userId) {
				this.$router.push(`/users/${userId}/edit/profile`);
			},
			goToWishlists(userId) {
				this.$router.push(`/users/${userId}/wishlists/all`);
			},
			goToListingDetails(listingId) {
                this.$router.push(`/listings/${listingId}`);
            }
		}
	};
</script>