/**
 * plugins/vuetify.js
 *
 * Framework documentation: https://vuetifyjs.com`
 */

// Styles
import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'

// Composables
import { createVuetify } from 'vuetify'

// Custom theme for the app
const purpleTheme = {
  dark: true,
  colors: {
    primary: '#514576',
    secondary: '#c7bde7',
    ternary: '#d3d3d3',
    success: '#d7ebba',
    warning: '#feffbe',
    error: '#d81e5b'
  },
}

// https://vuetifyjs.com/en/introduction/why-vuetify/#feature-guides
export default createVuetify({
  theme: {
    defaultTheme: 'purpleTheme',
    themes: {
      purpleTheme,
    },
  },
})
