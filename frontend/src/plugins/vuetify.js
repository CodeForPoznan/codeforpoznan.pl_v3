// eslint-disable-next-line
import 'vuetify/styles';
// eslint-disable-next-line
import * as components from 'vuetify/components';
// eslint-disable-next-line
import * as directives from 'vuetify/directives';
// eslint-disable-next-line
import { aliases, fa } from 'vuetify/iconsets/fa';
// eslint-disable-next-line
import { mdi } from 'vuetify/iconsets/mdi';
// eslint-disable-next-line
import { VDatePicker } from 'vuetify/labs/VDatePicker';

import '@mdi/font/css/materialdesignicons.css';
import { createVuetify } from 'vuetify';

const vuetify = createVuetify({
  components: {
    ...components,
    VDatePicker,
  },
  directives,
  icons: {
    defaultSet: 'fa',
    aliases,
    sets: {
      fa,
      mdi,
    },
  },
  ssr: true,
});

export default vuetify;
