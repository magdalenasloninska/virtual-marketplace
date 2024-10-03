<template>
    <Nav />

    <v-container class="pt-10">
        <v-row justify="center">
            <v-col cols="12" xl="8">
                <h3>Here you can see the matching search results!</h3>

                <v-spacer class="pa-4"></v-spacer>
                
                <v-container fluid>
                    <v-row>
                        <v-col
                            v-for="result in results"
                            :key="result.id"
                            :cols=12
                        >
                            <v-card
                                @click="goToListingDetails(result.id)"
                            >
                                <v-card-title class="text-white">
                                    {{ result.title }}
                                </v-card-title>
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
                listings: [],
                results: []
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
        // watch: {
        //     '$route.params.phrase': {
        //         handler: (newPhrase) => {
        //             this.performSearch(newPhrase);
        //         },
        //         immediate: true
        //     }
        // },
        methods: {
            performSearch(phrase) {
                for (const listing of this.listings) {
                    if (listing.title.includes(phrase)) {
                        this.results.push(listing);
                    }
                }
            },
            goToListingDetails(listingId) {
                this.$router.push(`/listings/${listingId}`);
            }
        }
    }
</script>