<template>
    <Nav />

    <v-container class="pt-10">
        <v-row justify="center" align="center">
            <v-col cols="8" xl="5">
                <v-card
                    class="request-bubble mx-10 mt-4"
                    style="overflow: visible;"
                >
                    <v-card-title>
                        <h3>grgrr</h3>
                    </v-card-title>
                    <v-card-text>
                        {{ this.exampleText }}
                    </v-card-text>
                </v-card>
            </v-col>

            <v-col cols="4" xl="3" class="d-flex justify-center">
                <v-avatar size="300">
                    <v-img
                        src="@/assets/museum.jpeg"
                    ></v-img>
                </v-avatar>
            </v-col>
        </v-row>

        <v-spacer class="pa-4"></v-spacer>

        <v-row justify="center">
            <v-col cols="12" xl="8">
                <h3>Here you can browse linked listings!</h3>

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
        z-index: 1;
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
</style>

<script>
    import axios from 'axios';

    export default {
        name: 'Listings',
        data() {
            return {
                listings: [],
                exampleText: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque placerat neque at mauris tristique sagittis. Donec nec pretium felis. In nec efficitur nisl. Morbi consectetur odio sapien, non blandit massa suscipit a. Fusce varius purus eu augue aliquam, eget bibendum erat sagittis. Cras sodales leo in risus finibus, eget feugiat leo faucibus. Sed fringilla mollis sollicitudin. Aenean vitae consequat dui. In hac habitasse platea dictumst. Etiam tristique laoreet eros vel tempor. Proin fermentum semper ligula non vehicula. Nunc at est dui. Phasellus at odio in eros bibendum elementum. Duis maximus enim quis ornare elementum. "
            };
        },
        mounted() {
            axios.get('http://localhost:8000/shop/api/listings/browse')
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
            }
        },
    };
</script>