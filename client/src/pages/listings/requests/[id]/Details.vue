<template>
    <Nav />

    <v-container class="pt-10">
        <v-container class="px-16">
            <v-row justify="center" align="center">
                <v-col cols="8" xl="5">
                    <v-card
                        class="request-bubble mt-4"
                        style="overflow: visible;"
                    >
                        <v-card-title class="handwritten px-8 pt-8">
                            <h3 v-if="!loading">
                                {{ requestDetails.title }}
                            </h3>
                            <h3 v-else>
                                A title or something
                            </h3>
                        </v-card-title>
                        <v-card-text class="px-8 pb-8">
                            <p v-if="!loading">
                                {{ requestDetails.description }}
                            </p>
                            <p v-else>
                                {{ this.exampleText }}
                            </p>
                        </v-card-text>
                    </v-card>
                </v-col>

                <v-col cols="4" xl="3" class="d-flex justify-center align-start">
                    <v-avatar size="200">
                        <v-img
                            v-if="loading"
                            src="@/assets/museum.jpeg"
                        ></v-img>
                        <v-img
                            v-else
                            :src="requestDetails.user.profile_picture"
                        ></v-img>
                    </v-avatar>
                </v-col>
            </v-row>
        </v-container>

        <v-spacer class="pa-4"></v-spacer>

        <v-row justify="center">
            <v-col cols="12" xl="8">
                <h3>Here you can browse linked listings!</h3>

                <v-container fluid>
                    <v-row>
                        <v-col
                            v-if="currentUser"
                            :cols=4
                        >
                            <v-card
                                class="plus-button"
                                height="100%"
                                width="100%"  
                                @click="goToSelection(requestId)"
                            >
                                <v-card-title>
                                    <h1>
                                        <v-icon>
                                            mdi-plus
                                        </v-icon>
                                    </h1>
                                </v-card-title>
                            </v-card>
                        </v-col>
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
                                    gradient="to bottom, rgba(0,0,0,0), rgba(0,0,0,.5)"
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
    .request-bubble {
        position: relative;
        background: #514576;
        border-radius: 20px;
    }

    .request-bubble:after {
        content: '';
        position: absolute;
        right: 0;
        top: 50%;
        width: 0;
        height: 0;
        border: 30px solid transparent;
        border-left-color: #514576;
        border-right: 0;
        margin-top: -30px;
        margin-right: -30px;
    }

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

    .handwritten {
        font-family: 'Homemade Apple', cursive;
    }
</style>

<script>
    import axios from 'axios';

    export default {
        name: 'Listings',
        data() {
            return {
                loading: true,
                currentUser: null,
                requestId: this.$route.params.id,
                requestDetails: null,
                linkedListings: [],
                exampleText: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque placerat neque at mauris tristique sagittis. Donec nec pretium felis. In nec efficitur nisl. Morbi consectetur odio sapien, non blandit massa suscipit a. Fusce varius purus eu augue aliquam, eget bibendum erat sagittis. Cras sodales leo in risus finibus, eget feugiat leo faucibus. Sed fringilla mollis sollicitudin. Aenean vitae consequat dui. In hac habitasse platea dictumst. Etiam tristique laoreet eros vel tempor. Proin fermentum semper ligula non vehicula. Nunc at est dui. Phasellus at odio in eros bibendum elementum. Duis maximus enim quis ornare elementum. "
            };
        },
        created() {
            this.getCurrentUser();
            this.fetchRequestDetails(this.requestId);
        },
        methods: {
            fetchRequestDetails(requestId) {
                axios.get(`http://localhost:8000/shop/api/listings/requests/${requestId}`)
                .then(response => {
                    this.requestDetails = response.data;
                    this.linkedListings = this.requestDetails.listings;
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
            goToSelection(requestId) {
                this.$router.push(`/listings/requests/${requestId}/select`);
            }
        },
    };
</script>