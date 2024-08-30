<template>
    <Nav />

    <v-container class="pt-10">
        <v-row justify="center">
            <v-col cols="12" xl="8">
                <h3>Here you can browse all listings!</h3>

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
                                    gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                                    aspect-ratio="1"
                                    cover
                                    >
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
                listings: [],
            };
        },
        mounted() {
            axios.get('http://localhost:8000/shop/api/listings/browse/apparel')
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
        },
    };
</script>