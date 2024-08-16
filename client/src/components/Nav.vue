<template>
    <v-app-bar>
        <v-tabs>
            <router-link to="/welcome" class="nav-link">
                <v-tab>
                    <v-icon>mdi-home</v-icon>
                </v-tab>
            </router-link>
            
            <router-link to="/browse" class="nav-link">
                <v-tab>
                    Apparel
                </v-tab>
            </router-link>

            <v-tab>Shoes</v-tab>
            <v-tab>Home</v-tab>
            <v-tab>Vintage</v-tab>

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
        </v-tabs>
    </v-app-bar>
</template>

<style>
    .nav-link {
        color: white;
    }
</style>