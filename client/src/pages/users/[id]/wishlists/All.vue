<template>
    <Nav />

    <v-container class="pt-10" :key="renderKey">
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
                
                <v-container fluid :key="renderKey">
                    <v-row>
                        <v-col
                            v-if="currentUser"
                            :cols=6
                        >
                            <v-card
                                class="plus-button"
                                height="100%"
                                width="100%"
                                @click=""
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
                                class="wishlist_card"
                                @click=""
                            >
                                <v-card-title>
                                    {{ wishlist.title }}
                                </v-card-title>

                                <v-card-subtitle>
                                    Last updated: ...
                                </v-card-subtitle>

                                <v-card-text>
                                    gfgfgfgfgffgggggggggggg
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
</style>

<script>
    import axios from 'axios';

    export default {
        data() {
            return {
                loading: true,
                userId: this.$route.params.id,
                newTitle: "New untitled list",
                wishlists: [],
                successAlert: false,
                errorAlert: false,
                renderKey: 0
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
                    console.error('Error fetching wishlists:', error);
                });
            },
            async createNewWishlist() {
                let formData = new FormData();
                formData.append('title', this.newTitle);
                
                let _ = await axios.post(`http://localhost:8000/shop/api/users/${this.userId}/wishlists/new/data`, formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                })
                .then(_ => {
                    this.successAlert = true;
                    this.errorAlert = false;

                    this.renderKey += 1;
                    this.fetchAllWishlists(this.userId);
                })
                .catch(error => {
                    console.error('Error creating new wishlist:', error);
                    this.successAlert = false;
                    this.errorAlert = true;
                });
            },
            deleteWishlist(wishlistId) {
                
            }
        }
    }
</script>