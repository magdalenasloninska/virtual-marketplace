<template>
    <Nav />

    <v-container class="pt-10">
        <v-row justify="center">
            <v-col cols="12" xl="8">
                <h3>Here you can browse all of the user's listings!</h3>

                <v-container fluid>
                    <v-row>
                        <v-col
                            v-for="listing in listings"
                            :key="listing.title"
                            :cols=4
                        >
                            <v-card
                                class="grid-item"
                                @click="goToListingDetails(listing.id)"
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
                                        {{listing.title}}
                                    </v-card-title>
                                    <v-card-text>
                                        {{listing.price}} €
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
        name: 'Listings',
        data() {
            return {
                userId: this.$route.params.id,
                listings: [],
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
        }
    };
</script>