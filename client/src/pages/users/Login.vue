<template>
    <Nav />

    <v-container class="pt-10">
        <v-row justify="center">
            <v-col cols="12" xl="8">
                <h3>Here you can login to your account!</h3>

                <v-spacer class="pa-4"></v-spacer>
                
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
                        color="rgb(199, 189, 231)"
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
                password: ''
            }
        },
        methods: {
            async loginUser() {
                let formData = new FormData();
                formData.append('username', this.username);
                formData.append('password', this.password);

                let _ = await axios.post("http://localhost:8000/shop/api/users/login/data", formData)
                .then(response => {
                    localStorage.setItem('access_token', response.data.access);
                    localStorage.setItem('refresh_token', response.data.refresh);

                    this.$router.push('/welcome');
                })
                .catch(error => {
                    console.error('Login error:', error);
                });
            }
        }
    }
</script>