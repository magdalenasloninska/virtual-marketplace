<template>
    <Nav />

    <v-container class="pt-10">
        <v-row justify="center">
            <v-col cols="12" xl="8">
                <h3>Time to confirm your order!</h3>

                <v-spacer class="pa-4"></v-spacer>
                
                <v-card>
                    <v-card-title>Order details</v-card-title>
                    <v-card-text>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam non urna orci. Nulla facilisi. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam non urna orci. Nulla facilisi. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam non urna orci. Nulla facilisi.</p>
                        <br>
                        <p>Suspendisse potenti. Duis vehicula orci nec dolor fermentum, ut feugiat turpis congue.</p>
                    </v-card-text>
                </v-card>

                <v-spacer class="pa-4"></v-spacer>

                <v-card>
                    <v-card-title>Payment methods</v-card-title>
                    <v-card-text>
                        <v-icon>mdi-credit-card-outline</v-icon>
                    </v-card-text>
                </v-card>

                <v-spacer class="pa-4"></v-spacer>

                <v-card>
                    <v-card-title>Delivery</v-card-title>
                    <v-card-text>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam non urna orci. Nulla facilisi. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam non urna orci. Nulla facilisi. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam non urna orci. Nulla facilisi.</p>
                        <br>
                        <p>Suspendisse potenti. Duis vehicula orci nec dolor fermentum, ut feugiat turpis congue.</p>
                    </v-card-text>
                </v-card>
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
                username: '',
                password: ''
            }
        },
        methods: {
            async loginUser() {
                let formData = new FormData();
                formData.append('username', this.username);
                formData.append('password', this.password);

                let _ = await axios.post("http://localhost:8000/shop/api/users/login/data", formData, {
                    headers: {
                        'X-CSRFToken': getCookie('csrftoken')
                    }
                });
            }
        }
    }
</script>