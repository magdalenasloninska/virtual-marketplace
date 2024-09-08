<template>
    <Nav />

    <v-container class="pt-10">
        <v-row justify="center">
            <v-col cols="12" xl="8">
                <h3>Here you can register and become a member!</h3>

                <v-spacer class="pa-4"></v-spacer>
                
                <form>
                    <v-text-field
                        label="Email address"
                        required
                        type="email"
                        prepend-icon="mdi-at"
                        v-model="email"
                    ></v-text-field>

                    <v-text-field
                        label="Username"
                        required
                        prepend-icon="mdi-format-letter-case"
                        v-model="username"
                    ></v-text-field>

                    <v-textarea
                        label="About"
                        variant="filled"
                        auto-grow
                        prepend-icon="mdi-text-box-edit"
                        rows="3"
                        v-model="about"
                    ></v-textarea>

                    <v-file-input
                        label="Profile picture"
                        v-model="profile_picture"
                    ></v-file-input>

                    <v-text-field
                        label="Password"
                        required
                        type="password"
                        v-model="password1"
                    ></v-text-field>

                    <v-text-field
                        label="Confirm password"
                        required
                        type="password"
                        v-model="password2"
                    ></v-text-field>

                    <v-spacer class="pa-4"></v-spacer>

                    <v-btn
                        class="me-4"
                        color="rgb(199, 189, 231)"
                        v-on:click="registerUser()"
                    >
                        Sign up
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
                email: '',
                username: '',
                about: '',
                profile_picture: null,
                password1: '',
                password2: ''
            }
        },
        methods: {
            async registerUser() {
                let formData = new FormData();
                formData.append('email', this.email);
                formData.append('username', this.username);
                formData.append('about', this.about);
                formData.append('profile_picture', this.profile_picture);
                formData.append('password', this.password1);

                let _ = await axios.post("http://localhost:8000/shop/api/users/register/data", formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                });
            }
        }
    }
</script>