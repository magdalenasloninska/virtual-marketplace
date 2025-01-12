<template>
    <Nav />

    <v-container class="pt-10">
        <v-row justify="center">
            <v-col cols="12" xl="8">
                <h3>Here you can see the user's reviews!</h3>

                <v-spacer class="pa-4"></v-spacer>
                
                <v-container fluid>
                    <v-row>
                        <v-col
                            v-for="review in reviews"
                            :key="review.id"
                            :cols=6
                        >
                            <v-card
                                variant="outlined"
                                rounded
                            >
                                <v-card-title class="text-white">
                                    <span style="display: flex; align-items: center;">
                                        <v-icon v-for="x in [1, 2, 3, 4, 5]">
                                            <template v-if="review.stars >= x">
                                                mdi-star
                                            </template>
                                            <template v-else-if="review.stars <= x + 0.5">
                                                mdi-star-half-full
                                            </template>
                                            <template v-else>
                                                mdi-star-outline
                                            </template>
                                        </v-icon>	
                                    </span>
                                </v-card-title>
                                <v-card-text>
                                    {{ review.comment }}
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
                userId: this.$route.params.id,
                reviews: []
            }
        },
        mounted() {
            this.fetchReviewsOfUser(this.userId);
        },
        methods: {
            fetchReviewsOfUser(userId) {
                axios.get(`http://localhost:8000/shop/api/users/${userId}/reviews`)
                    .then(response => {
                        this.reviews = response.data;
                    })
                    .catch(error => {
                        console.error('Error fetching reviews:', error);
                    });
            }
        }
    }
</script>