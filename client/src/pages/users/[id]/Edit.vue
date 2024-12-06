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
						<h1>
							{{ userDetails.username }}
							<v-btn
								class="ml-4"
								append-icon="mdi-check"
								@click="saveChanges()"
							>
								Save changes
							</v-btn>
						</h1>
					</v-card-title>
					<v-card-subtitle>
						<v-icon>mdi-star</v-icon>
						<v-icon>mdi-star</v-icon>
						<v-icon>mdi-star</v-icon>
						<v-icon>mdi-star-half-full</v-icon>
						<v-icon>mdi-star-outline</v-icon>
					</v-card-subtitle>
					<v-spacer class="mb-4"></v-spacer>
					<v-card-subtitle>
						<h2>Joined {{ dateJoined }}</h2>
					</v-card-subtitle>
					<v-card-text>
						<v-textarea
							variant="outlined" 
							rows="3"
							auto-grow
							v-model="newAbout"
						></v-textarea>
					</v-card-text>
				</v-card>
			</v-col>
		</v-row>
	
		<v-spacer class="my-8"></v-spacer>
	
		<v-container>
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
					v-for="x in [1, 2, 3]"
					:cols=4
				>
					<v-hover v-slot="{ isHovering, props }">
						<v-img
							src="@/assets/architecture.jpeg"
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
										<v-row class="justify-center text-h3 handwritten">
											<p
												class="wrap-text text-center"
											>
												Zwinger
											</p>
										</v-row>
										<v-row class="justify-center text-h5">
											<p>42 €</p>
										</v-row>
										<v-row class="justify-center pa-4">
											<v-btn
												variant="outlined"
											>
												Choose featured listing
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
				newAbout: "",
				dateJoined: null,
			};
		},
		created() {
			this.getCurrentUser();
			this.fetchUserDetails(this.userId);
		},
		methods: {
			fetchUserDetails(userId) {
				axios.get(`http://localhost:8000/shop/api/users/${userId}`)
				.then(response => {
					this.userDetails = response.data;
					this.newAbout = this.userDetails.about;
					let options = { year: 'numeric', month: 'long' };
					this.dateJoined = new Date(this.userDetails.date_joined).toLocaleDateString('en-US', options);
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
					console.error(`Error fetching current user: ${error}`);
				});
			},
			async saveChanges() {
				let formData = new FormData();
				formData.append('new_about', this.newAbout);

				let _ = await axios.post(`http://localhost:8000/shop/api/users/${this.userId}/edit/data`, formData, {
					headers: {
						'Content-Type': 'multipart/form-data'
					}
				})
				.then(_ => {
					this.$router.push(`/users/${this.userId}/profile`);
				})
				.catch(error => {
					console.error('Error updating user profile:', error);
				});
			}
		}
    };
  
</script>