<template>
    <Nav />

    <v-container class="pt-10">
        <v-row justify="center">
            <v-col cols="12" xl="8">
                <h3>Here you can select a listing to be featured!</h3>

                <v-container fluid>
                    <v-row>
                        <v-col
                            v-for="listing in listings.filter(listing => listing.featured == 0)"
                            :key="listing.title"
                            :cols=4
                        >
                            <v-card
                                class="grid-item"
                                @click="selectFeaturedListing(listing.id, position)"
                            >
                                <v-img
                                    :src="listing.photo"
                                    class="align-end"
                                    :gradient="getThumbnailGradient(listing.sold)"
                                    aspect-ratio="1"
                                    cover
                                >
                                    <v-chip
                                        v-if="listing.sold"
                                        size="x-large"
                                        variant="flat"
                                        color="success"
                                    >
                                        Item sold
                                    </v-chip>

                                    <v-card-title class="text-white">
                                        {{ listing.title }}
                                    </v-card-title>
                                    <v-card-text>
                                        {{ listing.price }} €
                                    </v-card-text>
                                </v-img>
                            </v-card>
                        </v-col>
                    </v-row>
                </v-container>
            </v-col>
        </v-row>
    </v-container>
</template>

<style>
    .grid-item {
        text-align: center;
        transition: transform 0.3s;
    }

    .grid-item:hover {
        transform: scale(1.05);
    }

    .square-thumbnail {
        height: 100%;
        object-fit: cover;
        object-position: center;
    }
</style>

<script>
    import axios from 'axios';

    export default {
        data() {
            return {
                userId: this.$route.params.id,
                listings: [],
                position: this.$route.params.pos
            };
        },
        mounted() {
            axios.get(`http://localhost:8000/shop/api/users/${this.userId}/listings`)
            .then(response => {
                this.listings = response.data;
            })
            .catch(error => {
                console.error('Error fetching listings:', error);
            });
        },
        methods: {
            goToListingDetails(listingId) {
                this.$router.push(`/listings/${listingId}`);
            },
            getThumbnailGradient(isSold) {
                return isSold
                    ? 'to bottom, rgba(0,0,0,0.55), rgba(0,0,0,.55)'
                    : 'to bottom, rgba(0,0,0,0), rgba(0,0,0,.5)';
            },
            async selectFeaturedListing(listingId, position) {
                let formData = new FormData();
				formData.append('listing_id', listingId);
                formData.append('position', position);
                console.log(`Position: ${position}`);

				let _ = await axios.post(`http://localhost:8000/shop/api/users/${this.userId}/featured/edit/data`, formData, {
					headers: {
						'Content-Type': 'multipart/form-data'
					}
				})
				.then(_ => {
					this.$router.push(`/users/${this.userId}/profile`);
				})
				.catch(error => {
					console.error('Error while choosing a featured listing:', error);
				});
            }
        }
    };
</script>