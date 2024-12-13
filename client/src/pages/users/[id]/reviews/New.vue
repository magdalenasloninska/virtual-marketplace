<template>
    <Nav />

    <v-container class="pt-10">
        <v-row justify="center">
            <v-col cols="12" xl="8">
                <h3>Here you can add your review of the seller!</h3>

                <v-spacer class="pa-4"></v-spacer>
                
                <div>       
                    <v-alert
                        v-if="errorAlert"
                        color="error"
                        type="error"
                        closable
                        class="mb-8"
                    >
                        {{ errorMessage }}
                    </v-alert>
                </div>

                <v-container>
                    <v-row>
                        <v-col cols="1">
                            <h1
                                class="rating"
                            >{{ stars }}</h1>
                        </v-col>
                        <v-col cols="3">
                            <v-rating
                                class="d-flex justify-center mb-4"
                                half-increments
                                hover
                                :length="5"
                                :size="59"
                                color="secondary"
                                active-color="#FFD700"
                                v-model="stars"
                            />
                        </v-col>
                    </v-row>
                </v-container>

                <v-textarea
                    label="Comment"
                    variant="filled"
                    auto-grow
                    prepend-icon="mdi-text-box-edit"
                    rows="3"
                    v-model="comment"
                ></v-textarea>

                <v-spacer class="pa-4"></v-spacer>

                <v-btn
                    color="secondary"
                >
                    Submit review
                </v-btn>
            </v-col>
        </v-row>
    </v-container>
</template>

<style>
    .rating {
        color: rgb(var(--v-theme-secondary));
    }
</style>

<script>
    import axios from 'axios';
    
    export default {
        data() {
            return {
                loading: true,
                userId: this.$route.params.id,
                stars: 0,
                comment: '',
                errorAlert: false,
                errorMessage: ''
            }
        },
        methods: {
            addReview() {

            }
        }
    }
</script>