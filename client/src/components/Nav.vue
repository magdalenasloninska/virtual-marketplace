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
    </v-app-bar>
</template>

<style>
    .nav-link {
        color: white;
    }
</style>