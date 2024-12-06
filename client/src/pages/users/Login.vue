<template>
    <Nav />

    <v-container class="pt-10">
        <v-row justify="center">
            <v-col cols="12" xl="8">
                <h3>Here you can login to your account!</h3>

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

                <form>
                    <v-text-field
                        label="Username"
                        required
                        v-model="username"
                    ></v-text-field>

                    <v-text-field
                        label="Password"
                        required
                        type="password"
                        v-model="password"
                    ></v-text-field>

                    <v-spacer class="pa-4"></v-spacer>

                    <v-btn
                        class="me-4"
                        color="secondary"
                        v-on:click.prevent="loginUser()"
                    >
                        Login
                    </v-btn>
                </form>
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
                password: '',
                errorAlert: false,
                errorMessage: ''
            }
        },
        methods: {
            async loginUser() {
                let formData = new FormData();
                formData.append('username', this.username);
                formData.append('password', this.password);

                let _ = await axios.post("http://localhost:8000/shop/api/users/login/data", formData)
                .then(response => {

                    if (response.data.success) {
                        localStorage.setItem('access_token', response.data.access);
                        localStorage.setItem('refresh_token', response.data.refresh);
                        this.$router.push('/welcome');
                    } else {
                        this.errorAlert = true;
                        this.errorMessage = response.data.message;
                    }
                })
                .catch(error => {
                    console.error('Login error:', error);
                });
            }
        }
    }
</script>