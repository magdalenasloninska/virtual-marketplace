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
                        @click="currentlyEditingTitle=true"
                    >
                        Create new list
                    </v-btn>

                    <v-text-field
                        v-if="currentlyEditingTitle"
                        class="mt-4"
                        clearable
                        label="Title of your new wishlist"
                        variant="outlined"
                        @keyup.enter="createNewWishlist()"
                        v-model="newTitle"
                    ></v-text-field>
                </h3>

                <v-spacer class="pa-4"></v-spacer>
                
                <v-container fluid :key="renderKey">
                    <v-row>
                        <v-col
                            v-for="wishlist in wishlists"
                            :key="wishlist.title"
                            :cols=6
                        >
                            <v-card
                                class="wishlist_card"
                                @click="goToWishlistDetails(wishlist.id)"
                            >
                                <v-card-title class="d-flex justify-space-between align-center typewriter">
                                    {{ wishlist.title }}
                                    <div>
                                        <v-btn
                                            class="ml-2"
                                            icon="mdi-pencil"
                                            color="ternary"
                                            variant="outlined"
                                            @click.stop="editWishlistTitle(wishlist.id)"
                                        ></v-btn>
                                        <v-btn
                                            class="ml-2"
                                            icon="mdi-trash-can"
                                            color="ternary"
                                            variant="outlined"
                                            @click.stop="deleteWishlist(wishlist.id)"
                                        ></v-btn>
                                    </div>
                                    
                                </v-card-title>

                                <v-card-subtitle>
                                    Last updated: ...
                                </v-card-subtitle>

                                <v-card-text>
                                    {{ wishlist.id }}
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
    .typewriter {
        font-family: 'Courier New', Courier, monospace;
    }
</style>

<script>
    import axios from 'axios';

    export default {
        data() {
            return {
                loading: true,
                userId: this.$route.params.id,
                newTitle: "",
                currentlyEditingTitle: false,
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

                    this.currentlyEditingTitle = false;
                    this.newTitle = "";
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
                axios.post(`http://localhost:8000/shop/api/wishlists/delete/${wishlistId}`)
                .then(_ => {
                    this.renderKey += 1;
                    this.fetchAllWishlists(this.userId);
                })
                .catch(error => {
                    console.error('Error deleting wishlist:', error);
                });
            },
            editWishlistTitle(wishlistId) {

            },
            goToWishlistDetails(wishlistId) {
                this.$router.push(`/users/${this.userId}/wishlists/${wishlistId}`);
            }
        }
    }
</script>