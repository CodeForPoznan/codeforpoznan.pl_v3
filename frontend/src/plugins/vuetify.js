// eslint-disable-next-line
import 'vuetify/styles'
// eslint-disable-next-line
import * as components from 'vuetify/components';
// eslint-disable-next-line
import * as directives from 'vuetify/directives';

import '@mdi/font/css/materialdesignicons.css';
import { createVuetify } from 'vuetify';

const vuetify = createVuetify({
  components,
  directives,
  icons: {
    iconfont: 'mdi',
  },
  ssr: true,
});

export default vuetify;
