<template>
    <Nav />

    <v-container class="pt-10">
        <v-row justify="center">
            <v-col cols="12" xl="8">
                <h3>Here you can see what others are looking for!</h3>

                <v-spacer class="pa-4"></v-spacer>
                
                <v-container fluid>
                    <v-row>
                        <v-col
                            v-for="request in requests"
                            :key="request.title"
                            :cols=6
                        >
                            <v-card
                                class="request_card"
                                ratio="1/1"
                                @click="goToRequestDetails()"
                            >
                                <v-card-title>
                                    {{ request.title }}
                                </v-card-title>

                                <v-card-subtitle>
                                    4 listings linked
                                </v-card-subtitle>

                                <v-card-text class="text-truncate">
                                    {{ exampleText }}
                                </v-card-text>
                            </v-card>
                        </v-col>
                    </v-row>
                </v-container>
            </v-col>
        </v-row>
    </v-container>
</template>

<style>
    .request_card {
        background-color: /* rgb(216, 30, 91); */ rgb(81, 69, 118);
        /* font-family: 'Courier New', Courier, monospace; */
    }
</style>

<script>
    import axios from 'axios';

    export default {
        data() {
            return {
                requests: [
                    {"title": "An example"},
                    {"title": "Another example"},
                    {"title": "Yet another"}
                ],
                exampleText: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque placerat neque at mauris tristique sagittis. Donec nec pretium felis. In nec efficitur nisl. Morbi consectetur odio sapien, non blandit massa suscipit a. Fusce varius purus eu augue aliquam, eget bibendum erat sagittis. Cras sodales leo in risus finibus, eget feugiat leo faucibus. Sed fringilla mollis sollicitudin. Aenean vitae consequat dui. In hac habitasse platea dictumst. Etiam tristique laoreet eros vel tempor. Proin fermentum semper ligula non vehicula. Nunc at est dui. Phasellus at odio in eros bibendum elementum. Duis maximus enim quis ornare elementum. "
            };
        },
        mounted() {
            // axios.get('http://localhost:8000/shop/api/listings/browse')
            // .then(response => {
            //     this.requests = response.data;
            // })
            // .catch(error => {
            //     console.error('Error fetching listings:', error);
            // });
        },
        methods: {
            goToListingDetails(listingId) {
                this.$router.push(`/listings/${listingId}`);
            },
            goToRequestDetails() {

            }
        }
    }
</script>