<template>
    <Nav />

    <v-container class="pt-10">
        <v-row justify="center">
            <v-col cols="12" xl="8">
                <h3>Here you can see your orders and review sellers!</h3>

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
                errorAlert: false,
                errorMessage: ''
            }
        },
        methods: {
        }
    }
</script>