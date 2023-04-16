import { helpers } from '@vuelidate/validators';

export const slackNickValidator = helpers.regex(
  /^[0-9A-Za-ząćęłńóśźżĄĆĘŁŃÓŚŹŻ,.';\-_/()[\]{}]*$/
);

export const gitHubUsernameValidator = helpers.regex(
  /^[0-9A-Za-z][0-9A-Za-z-]*[0-9A-Za-z]$/
);
