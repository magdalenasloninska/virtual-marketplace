<template>
    <Nav />

    <v-container class="pt-10">
        <v-row justify="center">
            <v-col cols="12" xl="8">
                <h3>Here you can see the matching search results!</h3>

                <v-spacer class="pa-4"></v-spacer>
                
                <v-container fluid :key="renderKey">
                    <v-row
                        v-if="results.length > 0"
                    >
                        <v-col
                            v-for="result in results"
                            :key="result.id"
                            :cols=12
                        >
                            <v-card
                                class="result_card"
                                append-icon="mdi-arrow-right"
                                @click="goToListingDetails(result.id)"
                            >
                                <v-card-title>
                                    {{ result.title }}
                                </v-card-title>
                            </v-card>
                        </v-col>
                    </v-row>
                    <v-row
                        v-else
                    >
                        <v-col>
                            <v-icon
                                size="x-large"
                            >
                                mdi-weather-windy
                            </v-icon>
                        </v-col>
                    </v-row>
                </v-container>
            </v-col>
        </v-row>
    </v-container>
</template>

<style>
    .result_card {
        background-color: rgb(var(--v-theme-secondary));
        color: black;
        font-family: 'Courier New', Courier, monospace;
    }
</style>

<script>
    import axios from 'axios';

    export default {
        data() {
            return {
                listings: [],
                results: [],
                renderKey: 0
            };
        },
        mounted() {
            axios.get('http://localhost:8000/shop/api/listings/browse')
            .then(response => {
                this.listings = response.data;
                this.performSearch(this.$route.params.phrase);
            })
            .catch(error => {
                console.error('Error fetching listings:', error);
            });
        },
        methods: {
            performSearch(phrase) {

                this.results = [];

                for (const listing of this.listings) {
                    if (listing.title.toLowerCase().includes(phrase.toLowerCase())) {
                        this.results.push(listing);
                    }
                }

                this.renderKey += 1;
            },
            goToListingDetails(listingId) {
                this.$router.push(`/listings/${listingId}`);
            }
        }
    }
</script>