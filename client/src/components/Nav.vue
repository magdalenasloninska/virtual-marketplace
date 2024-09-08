<template>
    <v-app-bar>
        <v-tabs>
            <router-link to="/welcome" class="nav-link">
                <v-tab>
                    <v-icon>mdi-home</v-icon>
                </v-tab>
            </router-link>
            
            <router-link to="/listings/browse/apparel" class="nav-link">
                <v-tab>
                    Apparel
                </v-tab>
            </router-link>

            <router-link to="/listings/browse/home" class="nav-link">
                <v-tab>
                    Home & lifestyle
                </v-tab>
            </router-link>

            <router-link to="/listings/browse/other" class="nav-link">
                <v-tab>
                    Other
                </v-tab>
            </router-link>

            <v-menu
                open-on-hover
            >
                <template v-slot:activator="{ props }">
                    <v-tab
                        color="primary"
                        v-bind="props"
                    >
                        Dropdown menu
                    </v-tab>
                </template>

                <v-list>
                    <v-list-item>
                        <v-list-item-title>Casual</v-list-item-title>
                        <v-list-item-title>Special occasion</v-list-item-title>
                        <v-list-item-title>Athletic</v-list-item-title>
                    </v-list-item>
                </v-list>
            </v-menu>

            <router-link to="/listings/new" class="nav-link">
                <v-tab>
                    <v-icon>mdi-plus</v-icon>
                </v-tab>
            </router-link>
        </v-tabs>

        <v-spacer></v-spacer>

        <v-menu>
            <template v-slot:activator="{ props }">
                <v-btn
                    v-bind="props"
                    icon
                    class="mr-4"
                >
                    <v-avatar
                        v-if="user !== null"
                    >
                        <v-img
                            :src="user.profile_picture"
                        ></v-img>
                    </v-avatar>
                    <v-avatar
                        v-else
                        color="white"
                        icon="mdi-account"
                    ></v-avatar>
                </v-btn>
            </template>
            <v-card max-width="250">
                <v-card-text>
                    <div class="mx-auto text-center" v-if="user">
                        <h3>{{ user.username }}</h3>
                    </div>

                    <div class="mx-auto text-center" v-else>
                        <h3>You're not currently logged in, wanna fix that?</h3>

                        <v-spacer class="pa-2"></v-spacer>

                        <router-link to="/users/login">
                            <v-btn
                                color="white"
                                rounded
                            >
                                Login
                            </v-btn>
                        </router-link>

                        <v-spacer class="pa-2"></v-spacer>

                        <router-link to="/users/register">
                            <v-btn
                                color="white"
                                variant="outlined"
                                rounded
                            >
                                Register
                            </v-btn>
                        </router-link>
                    </div>
                </v-card-text>
            </v-card>
        </v-menu>

    </v-app-bar>
</template>

<style>
    .nav-link {
        color: white;
    }
</style>

<script>
    import axios from 'axios';

    export default {
        data() {
            return {
                user: null
            };
        },
        mounted() {
            this.getCurrentUser();
        },
        methods: {
            getCurrentUser() {
                axios.get('http://localhost:8000/shop/api/users/current-user')
                    .then(response => {
                        if ('username' in response) {
                            this.user = response.data;
                        }
                    })
                    .catch(error => {
                        console.error(`Error fetching current user: ${error}`);
                    });
            }
        }
    }
</script>