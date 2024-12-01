<template>
	<Nav/>

	<v-container class="pt-10">
		<v-row justify="center">
			<v-col cols="6" xl="4">
				<v-responsive>
					<v-carousel height="600" width="600" hide-delimiters progress>
						<v-carousel-item>
							<v-img
								:src="listingDetails.photo"
								class="carousel-image"
							></v-img>
						</v-carousel-item>
					</v-carousel>
				</v-responsive>
			</v-col>

			<v-col cols="6" xl="4">
				<v-card v-if="!loading">
					<v-container
						v-if="!userLoading && currentUser.active_login"
					>
						<v-btn
							v-if="isCurrentUser"
							icon="mdi-pencil"
							variant="outlined"
							color="ternary"
						></v-btn> 

						<v-menu
							:close-on-content-click="false"
						>
							<template v-slot:activator="{ props }">
								<v-btn
									v-if="!isCurrentUser"
									v-bind="props"
									:icon="isHearted ? 'mdi-heart' : 'mdi-heart-outline'"
								></v-btn>
							</template>

							<v-card>
								<v-card-title>
									Select wishlist:
								</v-card-title>

								<v-container fluid>
									<v-row>
										<v-col
											v-for="wishlist in wishlists"
											cols="12"
										>
											<v-checkbox
												:label=wishlist.title
												:value=wishlist.id
												v-model="selectedWishlistId"
											></v-checkbox>
										</v-col>
									</v-row>
								</v-container>
							</v-card>
							<v-btn
								color="secondary"
								@click="linkListing(selectedWishlistId, listingId)"
							>
								Ok
							</v-btn>
						</v-menu>

					</v-container>

					<v-card-title class="text-wrap">
						<h1>{{ listingDetails.title }}
							<v-chip
								v-if="listingDetails.sold"
								class="ml-2 "
								size="x-large"
								variant="flat"
								color="success"
							>
								Item sold
							</v-chip>
						</h1>
					</v-card-title>
					<v-card-subtitle>
						<h2>{{ listingDetails.price }} €</h2>
					</v-card-subtitle>
					<v-card-text>
						{{ listingDetails.description }}
					</v-card-text>
				</v-card>

				<v-spacer class="my-4"></v-spacer>

				<v-card
					@click="goToseller(seller.id)"
				>
					<v-card-subtitle class="mt-4">
						<h2>About the seller</h2>
					</v-card-subtitle>
					<v-card-text>
						<v-row justify="center">
							<v-col cols="2" class="d-flex justify-center align-center">
								<v-avatar size="70">
									<v-img
										:src="seller.profile_picture"
									></v-img>
								</v-avatar>
							</v-col>
							<v-col>
								<h1>{{ seller.username }}</h1>
								<div>
									<v-icon>mdi-star</v-icon>
									<v-icon>mdi-star</v-icon>
									<v-icon>mdi-star</v-icon>
									<v-icon>mdi-star-half-full</v-icon>
									<v-icon>mdi-star-outline</v-icon>
								</div>
							</v-col>
						</v-row>
					</v-card-text>
				</v-card>

				<v-spacer class="my-8"></v-spacer>

				<v-container
					v-if="!isCurrentUser && !listingDetails.sold"
					class="pa-0"
				>
					<v-btn
						block
						color="secondary"
						rounded
						class="pa-4"
						@click="createOrder(listingId)"
					>
						Buy now
					</v-btn>

					<v-spacer class="my-4"></v-spacer>

					<v-btn
						block
						variant="outlined"
						color="secondary"
						rounded
						class="pa-4"
					>
						Ask a question
					</v-btn>
				</v-container>
			</v-col>
		</v-row>
	</v-container>

</template>

<style scoped>
	.carousel-image {
		object-fit: contain;
		max-width: 100%;
		max-height: 100%;
		width: auto;
		height: auto;
		display: block;
		margin: auto;
	}

	.image-container {
		display: flex;
		justify-content: center;
		align-items: center;
		height: 100%;
		width: 100%;
	}
</style>

<script>
	import axios from 'axios';

	import Nav from '@/components/Nav.vue'

	export default {
    	data() {
			return {
				loading: true,
				userLoading: true,
				currentUser: [],
				isCurrentUser: false,
				listingId: this.$route.params.id,
				listingDetails: [],
				seller: [],
				isHearted: false,
				wishlists: [],
				selectedWishlistId: null
			};
		},
		async created() {
			await this.getCurrentUser();
			await this.fetchListingDetails(this.listingId);
		},
		methods: {
			fetchListingDetails(listingId) {
				axios.get(`http://localhost:8000/shop/api/listings/${listingId}`)
					.then(response => {
						this.listingDetails = response.data;
						this.seller = this.listingDetails.user;
						this.loading = false;

						if (this.currentUser !== null) {
							this.isCurrentUser = (this.seller.username == this.currentUser.username);
						}
					})
					.catch(error => {
						console.error('Error fetching listing details:', error);
					});
			},
			toggleHeart() {
				this.isHearted = !this.isHearted;
			},
			goToseller(userId) {
				this.$router.push(`/users/${userId}/profile`);
			},
			createOrder(listingId) {
				this.$router.push(`/order/${listingId}/create`);
			},
			getCurrentUser() {
				axios.get('http://localhost:8000/shop/api/users/current-user')
					.then(response => {
						this.currentUser = response.data;
						this.fetchAllWishlists(this.currentUser.id);
						this.userLoading = false;
					})
					.catch(error => {
						console.error(`Error fetching current user: ${error}`);
					});
			},
			fetchAllWishlists(userId) {
				axios.get(`http://localhost:8000/shop/api/users/${userId}/wishlists`)
				.then(response => {
					this.wishlists = response.data;
					this.loading = false;
				})
				.catch(error => {
					console.error('Error fetching wishlists:', error);
				});
			},
			async linkListing(wishlistId, listingId) {
				let formData = new FormData();
				formData.append('listing_id', listingId);

				let _ = await axios.post(`http://localhost:8000/shop/api/wishlists/${wishlistId}/new/data`, formData, {
					headers: {
						'Content-Type': 'multipart/form-data'
					}
				})
				.then(_ => {
					// this.$router.push(`/listings/requests/${this.requestId}/details`);
					this.isHearted = true;
				})
				.catch(error => {
					console.error('Error linking new listing:', error);
				});
			}
		}
  	};

</script>