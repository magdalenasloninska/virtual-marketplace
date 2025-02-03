<template>
    <Nav />

    <v-container class="pt-10">
        <v-row justify="center">
            <v-col cols="12" xl="8">

                <v-card class="mb-10 title-card">
                    <v-card-title
                        class="d-flex justify-center typewriter"
                    >
                        <h1
                            v-if="!loading"
                        >
                            "{{ wishlistDetails.title }}"
                        </h1>
                    </v-card-title>
                </v-card>

                <h3>Here you can browse linked listings!</h3>

                <v-container fluid>
                    <v-row>
                        <v-col
                            v-for="listing in linkedListings"
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

    .plus-button {
        border-radius: 0;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .typewriter {
        font-family: 'Courier New', Courier, monospace;
    }

    .handwritten {
        font-family: 'Homemade Apple', cursive;
    }

    .title-card {
        background-color: rgb(var(--v-theme-ternary));
        color: black;
    }
</style>

<script>
    import axios from 'axios';

    export default {
        data() {
            return {
                loading: true,
                currentUser: null,
                wishlistId: this.$route.params.name,
                wislistDetails: null,
                linkedListings: []
            };
        },
        created() {
            this.getCurrentUser();
            this.fetchWishlistDetails(this.wishlistId);
        },
        methods: {
            fetchWishlistDetails(wishlistId) {
                axios.get(`http://localhost:8000/shop/api/wishlists/${wishlistId}`)
                .then(response => {
                    this.wishlistDetails = response.data;
                    this.linkedListings = this.wishlistDetails.content;
                    this.loading = false;
                })
                .catch(error => {
                    console.error('Error fetching request details:', error);
                });
            },
            goToListingDetails(listingId) {
                this.$router.push(`/listings/${listingId}`);
            },
            getCurrentUser() {
                axios.get('http://localhost:8000/shop/api/users/current-user')
                .then(response => {
                    this.currentUser = response.data;
                })
                .catch(error => {
                    console.error(`Error fetching current user: ${error}`);
                });
            },
            getThumbnailGradient(isSold) {
                return isSold
                    ? 'to bottom, rgba(0,0,0,0.55), rgba(0,0,0,.55)'
                    : 'to bottom, rgba(0,0,0,0), rgba(0,0,0,.5)';
            }
        },
    };
</script>