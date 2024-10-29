<template>
    <Nav />

    <v-container class="pt-10">
        <v-row justify="center">
            <v-col cols="12" xl="8">
                <h3>
                    Here you can select which of your listings to promote!

                    <v-btn
                        class="ml-4"
                        append-icon="mdi-check"
                        color="rgb(199, 189, 231)"
                        @click="linkListing(selectedListingId)"
                    >
                        Save my choice
                    </v-btn>
                </h3>

                <v-spacer class="pa-4"></v-spacer>
                
                <v-container fluid>
                    <v-row>
                        <v-col
                            v-for="listing in listings"
                            cols="12"
                        >
                            <v-card class="d-flex justify-center">
                                <v-card-text>
                                    <v-checkbox
                                        :label=listing.title
                                        :value=listing.id
                                        v-model="selectedListingId"
                                    ></v-checkbox>
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
                currentUser: null,
                requestId: this.$route.params.id,
                listings: [],
                selectedListingId: null,
                successAlert: false,
                errorAlert: false
            }
        },
        mounted() {
            this.getCurrentUser();
        },
        methods: {
            getCurrentUser() {
                axios.get('http://localhost:8000/shop/api/users/current-user')
                .then(response => {
                    this.currentUser = response.data;
                    this.getListingsOfUser(this.currentUser.id);
                })
                .catch(error => {
                    console.error(`Error fetching current user: ${error}`);
                });
            },
            getListingsOfUser(userId) {
                axios.get(`http://localhost:8000/shop/api/users/${userId}/listings`)
                .then(response => {
                    this.listings = response.data;
                })
                .catch(error => {
                    console.error('Error fetching listings:', error);
                });
            },
            async linkListing(listingId) {
                let formData = new FormData();
                formData.append('listing_id', listingId);

                let _ = await axios.post(`http://localhost:8000/shop/api/listings/requests/${this.requestId}/new/data`, formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                })
                .then(_ => {
                    this.$router.push(`/listings/requests/${this.requestId}/details`);
                })
                .catch(error => {
                    console.error('Error linking new listing:', error);
                });
            }
        }
    }
</script>