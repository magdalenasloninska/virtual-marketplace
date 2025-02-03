<template>
    <Nav />

    <v-container class="pt-10">
        <v-row justify="center">
            <v-col cols="12" xl="8">
                <h3>Here you can see your orders and review sellers!</h3>

                <v-spacer class="pa-4"></v-spacer>
                
                <v-container>
                    <v-row>
                        <v-col
                            v-for="order in orders"
                            :key="order.title"
                            :cols=12
                        >
                            <v-card
                                class="order_card"
                                @click="redirectToReview(order.listing.id)"
                            >
                                <v-card-title>
                                    Item: {{ order.listing.title }}
                                </v-card-title>

                                <v-card-subtitle class="mb-4">
                                    Seller: {{ order.listing.user.username }}
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
                currentUser: null,
                orders: [],
                errorAlert: false,
                errorMessage: ''
            }
        },
        mounted() {
            this.getCurrentUser();
            
            axios.get(`http://localhost:8000/shop/api/users/${this.userId}/orders`)
            .then(response => {
                this.orders = response.data;
            })
            .catch(error => {
                console.error('Error fetching orders:', error);
            });
        },
        methods: {
            getCurrentUser() {
                axios.get('http://localhost:8000/shop/api/users/current-user')
                .then(response => {
                    this.currentUser = response.data;
                    this.loading = false;
                })
                .catch(error => {
                    console.error(`Error fetching current user: ${error}`);
                });
            },
            redirectToReview(listingId) {
                this.$router.push(`/orders/${listingId}/review`);
            }
        }
    }
</script>