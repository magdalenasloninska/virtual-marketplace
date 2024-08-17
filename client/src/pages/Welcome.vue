<template>
    <Nav />

    <v-container class="pt-10">
        <v-row justify="center">
            <v-col cols="12">
                <h1>Welcome to the most stylish corner of the internet!</h1>
                <v-spacer class="pa-4"></v-spacer>
                <v-btn
                    class="welcome_page_btn typewriter pa-4"
                    block
                    size="x-large"
                >
                    I'm buying
                </v-btn>
                <v-spacer class="pa-4"></v-spacer>
                <v-btn
                    class="welcome_page_btn handwritten pa-4"
                    block
                    size="x-large"
                >
                    I'm selling
                </v-btn>
            </v-col>
        </v-row>
    </v-container>
</template>

<style>
    .welcome_page_btn {
        
        font-size: 32px;
        text-transform: none;
    }

    .typewriter {
        font-family: 'Courier New', Courier, monospace;
    }

    .handwritten {
        font-family: 'Homemade Apple', cursive;
    }
</style>