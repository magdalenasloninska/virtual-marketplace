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
                        v-model="email"
                    ></v-text-field>

                    <v-text-field
                        label="Username"
                        required
                        v-model="username"
                    ></v-text-field>

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
                password1: '',
                password2: ''
            }
        }
    }
</script>