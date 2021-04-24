import { helpers } from 'vuelidate/lib/validators';

export const slackNickValidator = helpers.regex(
  'slackNickValidator',
  /^[0-9A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ,.';\-_/()[\]{}]*$/
);

export const gitHubUsernameValidator = helpers.regex(
  'gitHubUsernameValidator',
  /^[0-9A-Za-z][0-9A-Za-z-]*[0-9A-Za-z]$/
);
