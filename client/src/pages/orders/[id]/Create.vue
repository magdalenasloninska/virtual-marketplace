<template>
    <Nav />

    <v-container class="pt-10">
        <v-row justify="center">
            <v-col cols="12" xl="8">
                <h3>Time to confirm your order!</h3>

                <v-spacer class="pa-4"></v-spacer>
                
                <v-stepper
                    :items=stepperItems
                >
                    <template v-slot:item.1>
                        <v-card>
                            <v-card-title>Item details</v-card-title>
                            
                            <div v-if="!loading">
                                <v-card-text>
                                    Name: <b>{{ listingDetails.title }}</b>
                                    <br>
                                    Price: <b>{{ listingDetails.price }}</b>
                                </v-card-text>

                                <v-img
                                    :src="listingDetails.photo"
                                    height="300"
                                    width="300"
                                    class="rounded-xl mt-2 ml-3"
                                    cover
                                ></v-img>
                            </div>
                        </v-card>
                    </template>

                    <template v-slot:item.2>
                        <v-card>
                            <v-card-title>Delivery</v-card-title>
                            <v-card-text>
                                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam non urna orci. Nulla facilisi. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam non urna orci. Nulla facilisi. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam non urna orci. Nulla facilisi.</p>
                                <br>
                                <p>Suspendisse potenti. Duis vehicula orci nec dolor fermentum, ut feugiat turpis congue.</p>

                                <v-spacer class="pa-4"></v-spacer>

                                <v-btn-toggle
                                    v-model="deliveryOption"
                                    color="primary"
                                    rounded="0"
                                    group
                                >
                                    <v-btn value=0>
                                        Delivery option 1<br>
                                        10 €
                                    </v-btn>

                                    <v-btn value=1>
                                        Delivery option 2<br>
                                        12 €
                                    </v-btn>

                                    <v-btn value=2>
                                        Delivery option 3<br>
                                        13 €
                                    </v-btn>
                                </v-btn-toggle>
                                
                                <v-spacer class="pa-4"></v-spacer>

                                <v-row>
                                    <v-col cols="6">
                                        <form>
                                            <v-text-field
                                                label="First name"
                                                required
                                            ></v-text-field>

                                            <v-text-field
                                                label="Last name"
                                                required
                                            ></v-text-field>

                                            <v-text-field
                                                label="Country"
                                                required
                                                prepend-icon="mdi-map-marker"
                                            ></v-text-field>

                                            <v-text-field
                                                label="Postal code"
                                                required
                                            ></v-text-field>
                                        </form>
                                    </v-col>
                                </v-row>
                            </v-card-text>
                        </v-card>
                    </template>

                    <template v-slot:item.3>
                        <v-card>
                            <v-card-title>Payment methods</v-card-title>
                            <v-card-text>
                                <p>Amount to pay: <b>45 €</b></p>

                                <v-spacer class="pa-4"></v-spacer>

                                <v-row>
                                    <v-col cols="6">
                                        <form>
                                            <v-text-field
                                                label="Cardholder"
                                                required
                                                prepend-icon="mdi-account"
                                            ></v-text-field>

                                            <v-text-field
                                                label="Card number"
                                                required
                                                prepend-icon="mdi-credit-card-outline"
                                                hint="Format: 1234 5678 9012 3456"
                                                persistent-hint
                                            ></v-text-field>

                                            <v-text-field
                                                label="Expiration date"
                                                required
                                                prepend-icon="mdi-calendar-blank"
                                            ></v-text-field>
                                        </form>
                                    </v-col>
                                </v-row>
                            </v-card-text>
                        </v-card>
                    </template>
                </v-stepper>

                <div>
                    <v-btn
                        class="mt-8 mr-4"
                        color="secondary"
                        :disabled="isLastStep"
                        @click="initTransaction(listingId)"
                    >
                        Order
                    </v-btn>

                    <v-btn
                        class="mt-8"
                        color="secondary"
                        variant="outlined"
                        @click="this.$router.push(`/listings/${listingId}`);"
                    >
                        Back to listing
                    </v-btn>
                </div>
            </v-col>
        </v-row>
    </v-container>
</template>

<style>
</style>

<script>
    import axios from 'axios';

    export default {
        data() {
            return {
                loading: true,
                listingDetails: null,
                listingId: this.$route.params.id,
                stepperItems: ["Item details", "Delivery", "Payment methods"],
                isLastStep: false,
                deliveryOption: 0
            }
        },
        mounted() {
            this.fetchListingDetails(this.listingId);
        },
        methods: {
            fetchListingDetails(listingId) {
				axios.get(`http://localhost:8000/shop/api/listings/${listingId}`)
					.then(response => {
						this.listingDetails = response.data;
						this.loading = false;
					})
					.catch(error => {
						console.error('Error fetching listing details:', error);
					});
			},
            async initTransaction(listingId) {
                let formData = new FormData();
				formData.append('listing_id', listingId);

				let _ = await axios.post(`http://localhost:8000/shop/api/transactions/new/data`, formData, {
					headers: {
						'Content-Type': 'multipart/form-data'
					}
				})
				.then(_ => {
					this.redirectToReview(this.listingDetails.user.id);
				})
				.catch(error => {
					console.error('Error initializing transaction:', error);
				});
            },
            redirectToReview(userId) {
                this.$router.push(`/users/${userId}/reviews/new`);
            }
        }
    }
</script>