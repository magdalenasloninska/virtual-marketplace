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
                            v-if="currentUser"
                            :cols=6
                        >
                            <v-card
                                class="plus-button"
                                height="100%"
                                width="100%"
                                @click="goToCreatingNewRequest()"
                            >
                                <v-card-title class="handwritten">
                                    <h3>
                                        Help me find...
                                    </h3>
                                </v-card-title>
                            </v-card>
                        </v-col>
                        <v-col
                            v-for="request in requests"
                            :key="request.title"
                            :cols=6
                        >
                            <v-card
                                class="request_card"
                                @click="goToRequestDetails(request.id)"
                            >
                                <v-card-title>
                                    {{ request.title }}
                                </v-card-title>

                                <v-card-subtitle>
                                    {{ request.linked_listings_count }} listings linked
                                </v-card-subtitle>

                                <v-card-text class="text-truncate">
                                    {{ request.description }}
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
        background-color: rgb(var(--v-theme-primary));
        /* font-family: 'Courier New', Courier, monospace; */
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
        data() {
            return {
                currentUser: null,
                requests: [],
                exampleText: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque placerat neque at mauris tristique sagittis. Donec nec pretium felis. In nec efficitur nisl. Morbi consectetur odio sapien, non blandit massa suscipit a. Fusce varius purus eu augue aliquam, eget bibendum erat sagittis. Cras sodales leo in risus finibus, eget feugiat leo faucibus. Sed fringilla mollis sollicitudin. Aenean vitae consequat dui. In hac habitasse platea dictumst. Etiam tristique laoreet eros vel tempor. Proin fermentum semper ligula non vehicula. Nunc at est dui. Phasellus at odio in eros bibendum elementum. Duis maximus enim quis ornare elementum. "
            };
        },
        mounted() {
            this.getCurrentUser();
            
            axios.get('http://localhost:8000/shop/api/listings/requests/all')
            .then(response => {
                this.requests = response.data;
            })
            .catch(error => {
                console.error('Error fetching requests:', error);
            });
        },
        methods: {
            getCurrentUser() {
                axios.get('http://localhost:8000/shop/api/users/current-user')
                .then(response => {
                    this.currentUser = response.data;
                })
                .catch(error => {
                    console.error(`Error fetching current user: ${error}`);
                });
            },
            goToCreatingNewRequest() {
                this.$router.push('/listings/requests/new');
            },
            goToRequestDetails(requestId) {
                this.$router.push(`/listings/requests/${requestId}/details`);
            }
        }
    }
</script>