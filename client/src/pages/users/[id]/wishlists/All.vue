<template>
    <Nav />

    <v-container class="pt-10">
        <v-row justify="center">
            <v-col cols="12" xl="8">
                <h3>
                    Here you can look through your wishlists!
                
                    <v-btn
                        class="ml-4"
                        append-icon="mdi-plus"
                        @click="createNewWishlist()"
                    >
                        Create new list
                    </v-btn>
                </h3>

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
                            v-for="wishlist in wishlists"
                            :key="wishlist.title"
                            :cols=6
                        >
                            <v-card
                                class="request_card"
                                @click="goToRequestDetails(request.id)"
                            >
                                <v-card-title>
                                    {{ wishlist.title }}
                                </v-card-title>

                                <v-card-subtitle>
                                    Last updated: ...
                                </v-card-subtitle>
                            </v-card>
                        </v-col>
                    </v-row>
                </v-container>
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
                userId: this.$route.params.id,
                wishlists: []
            }
        },
        mounted() {
            this.fetchAllWishlists(this.userId);
        },
        methods: {
            fetchAllWishlists(userId) {
                axios.get(`http://localhost:8000/shop/api/users/${userId}/wishlists`)
                .then(response => {
                    this.wishlists = response.data;
                    this.loading = false;
                })
                .catch(error => {
                    console.error('Error fetching requests:', error);
                });
            },
            createNewWishlist() {
                
            }
        }
    }
</script>