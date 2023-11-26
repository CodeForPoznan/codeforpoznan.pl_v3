<template>
  <v-container class="pa-6">
    <v-row align="center" justify="center" class="pt-6">
      <v-col>
        <v-alert
          type="error"
          :model-value="!!getError"
          closable
          transition="slide-y-transition"
          :text="getError"
        ></v-alert>
      </v-col>
    </v-row>
    <v-row align="center" justify="center">
      <v-col>
        <v-alert
          type="warning"
          :model-value="warningAlert"
          v-model="warningAlert"
          closable
          @click="warningAlert = !warningAlert"
          transition="slide-y-transition"
          >{{ warningMessage }}</v-alert
        >
        <v-alert
          type="success"
          :model-value="!!successAlert"
          closable
          @click="successAlert = ''"
          transition="slide-y-transition"
          :text="successAlert"
        ></v-alert>
      </v-col>
    </v-row>

    <v-card>
      <v-tabs
        bg-color="#0CAEE7"
        density="comfortable"
        centered
        grow
        dark
        stacked
        icons-and-text
        v-model="selectedTab"
        height="75"
      >
        <v-tab
          @click.stop="
            editParticipant && formIsNotEmpty() && participantChanged()
              ? (dialog = true)
              : editParticipant
              ? ((editParticipant = false), resetForm())
              : null
          "
        >
          <v-icon icon="fas fa-user-plus"></v-icon>
          Create new participant
        </v-tab>

        <v-tab
          @click="
            formIsNotEmpty()
              ? (dialog = true)
              : ((editParticipant = true), v$.$reset())
          "
        >
          <v-icon icon="fas fa-user-edit"></v-icon>
          Edit existing participant
        </v-tab>
      </v-tabs>
      <v-card-text v-if="editParticipant">
        <ParticipantsSearch v-model="selectedParticipant" />
      </v-card-text>
      <v-divider></v-divider>
      <v-form @keyup.enter="onSubmit" class="pa-6">
        <v-text-field
          variant="underlined"
          color="#0CAEE7"
          v-model="form.email"
          label="E-mail"
          required
          :error-messages="v$.form.email.$errors.map((e) => e.$message)"
          @input="v$.form.email.$touch()"
          @blur="v$.form.email.$touch()"
        />
        <v-text-field
          variant="underlined"
          color="#0CAEE7"
          label="Github username"
          v-model="form.github_username"
          @blur="validateGithub($event)"
          :error-messages="
            v$.form.github_username.$errors.map((e) => e.$message)
          "
        />
        <v-text-field
          variant="underlined"
          color="#0CAEE7"
          label="First name"
          v-model="form.first_name"
          @blur="v$.form.first_name.$touch()"
          :error-messages="v$.form.first_name.$errors.map((e) => e.$message)"
        />
        <v-text-field
          variant="underlined"
          color="#0CAEE7"
          label="Last name"
          v-model="form.last_name"
          @blur="validateLastName($event)"
          :error-messages="v$.form.last_name.$errors.map((e) => e.$message)"
        />
        <v-text-field
          variant="underlined"
          color="#0CAEE7"
          label="Slack nick"
          v-model="form.slack"
          @blur="validateSlack($event)"
          :error-messages="v$.form.slack.$errors.map((e) => e.$message)"
        />
        <v-text-field
          variant="underlined"
          color="#0CAEE7"
          label="Phone No."
          v-model="form.phone"
          :counter="9"
          @blur="validatePhone($event)"
          :error-messages="v$.form.phone.$errors.map((e) => e.$message)"
        />
        <v-card-actions class="pt-3 align-center justify-center">
          <v-btn
            v-if="editParticipant"
            :disabled="v$.$invalid || !selectedParticipant"
            @click="onEditParticipant"
            class="add-participant-btn align-center justify-center"
            >Save changes</v-btn
          >
          <v-btn
            v-else
            :disabled="v$.$invalid"
            @click="onSubmit"
            class="add-participant-btn align-center justify-center"
            >Add new participant</v-btn
          >
        </v-card-actions>
      </v-form>
    </v-card>
    <v-dialog v-model="dialog" max-width="500">
      <v-card>
        <v-card-title class="headline"> Discard edit changes? </v-card-title>

        <v-card-text>
          If You click discard all unsaved changes will be lost.
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn
            color="#607d8b"
            text
            @click="
              resetForm();
              editParticipant = !editParticipant;
              dialog = false;
            "
          >
            Discard changes
          </v-btn>

          <v-btn
            color="#607d8b"
            text
            @click="
              selectedTab = 1;
              dialog = false;
            "
          >
            Back to edit
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import ParticipantsSearch from './ParticipantsSearch/ParticipantsSearch.vue';
import { mapGetters } from 'vuex';
import {
  required,
  minLength,
  maxLength,
  email,
  numeric,
  helpers,
} from '@vuelidate/validators';
import _ from 'lodash';
import {
  slackNickValidator,
  gitHubUsernameValidator,
} from '../../../helpers/validation';
import { useVuelidate } from '@vuelidate/core';
import { reactive } from 'vue';

export default {
  setup() {
    const form = reactive({
      email: '',
      github_username: '',
      first_name: '',
      last_name: '',
      slack: '',
      phone: '',
    });

    return { v$: useVuelidate(), form };
  },
  data() {
    return {
      warningAlert: false,
      warningMessage: '',
      successAlert: '',
      selectedParticipant: null,
      editParticipant: false,
      dialog: false,
      selectedTab: 0,
    };
  },
  components: {
    ParticipantsSearch,
  },
  validations() {
    const emailExists = (value) => {
      const exists = this.editParticipant
        ? true
        : !Object.values(this.getParticipants).find(
            (user) => user.email === value
          );

      return exists;
    };
    const githubExists = (value) => {
      return this.editParticipant
        ? true
        : !Object.values(this.getParticipants).find(
            (user) => user.github_username === value
          );
    };

    return {
      form: {
        email: {
          required: helpers.withMessage('This field cannot be empty', required),
          email: helpers.withMessage('Type a correct e-mail address', email),
          emailExists: helpers.withMessage('User already exists', emailExists),
        },
        github_username: {
          required,
          gitHubUsernameValidator: helpers.withMessage(
            'Invalid username',
            gitHubUsernameValidator
          ),
          githubExists: helpers.withMessage(
            'User with that github username already exists',
            githubExists
          ),
        },
        first_name: {
          required,
          minLength: minLength(3),
          maxLength: maxLength(25),
        },
        last_name: {
          required,
          minLength: minLength(3),
          maxLength: maxLength(25),
        },
        slack: {
          slackNickValidator,
          minLength: minLength(3),
          maxLength: maxLength(25),
        },
        phone: {
          numeric,
          minLength: minLength(9),
          maxLength: maxLength(9),
        },
      },
    };
  },
  methods: {
    onPopulateForm() {
      if (this.selectedParticipant) {
        this.editParticipant = true;
        this.$store
          .dispatch('participant/getParticipant', this.selectedParticipant.id)
          .then(() => {
            const selectedParticipant = this.getParticipant;

            Object.keys(this.form).map((key) => {
              this.form[key] = selectedParticipant[key];
            });
          });
      }
    },
    onEditParticipant() {
      this.$store
        .dispatch('participant/editParticipant', { ...this.form })
        .then((status) => {
          if (status === 200) {
            this.successAlert = 'Participant has been successfully edited';
            this.resetForm();
            setTimeout(() => (this.successAlert = ''), 5000);
          }
        });
    },
    onSubmit() {
      if (!this.v$.$invalid) {
        if (this.form.phone === '') this.form.phone = null;
        if (this.form.slack === '') this.form.slack = null;
        const newParticipantData = this.form;

        this.$store
          .dispatch('participant/createParticipant', newParticipantData)
          .then((status) => {
            if (status === 201) {
              this.successAlert = 'Participant has been successfully added';
              this.resetForm();
              setTimeout(() => (this.successAlert = ''), 5000);
            }
          });
      }
    },
    resetForm() {
      this.v$.$reset();
      this.selectedParticipant = null;
      Object.keys(this.form).map((key) => {
        this.form[key] = '';
      });
    },
    formIsNotEmpty() {
      return !Object.values(this.v$.form.$model).every(
        (x) => x === null || x === '' || x === undefined
      );
    },
    participantChanged() {
      if (!this.selectedParticipant) {
        return false;
      } else {
        return !_.isMatch(this.getParticipant, this.v$.form.$model);
      }
    },
    validateGithub(event) {
      this.v$.form.github_username.$touch();
      return (this.form.github_username = event.target.value.replace(
        /https?:\/\/github.com\//,
        ''
      ));
    },
    validateSlack($event) {
      this.v$.form.slack.$touch();
      if (
        Object.values(this.getParticipants).find(
          (user) => user.slack === $event.target.value
        ) &&
        !this.editParticipant
      )
        this.warningAlert = true;
      this.warningMessage =
        'This slack nick already exists. Please suggest change of the nick to avoid confusion on Slack';
      setTimeout(() => (this.warningAlert = false), 10000);
    },
    validateLastName($event) {
      this.v$.form.last_name.$touch();
      if (
        Object.values(this.getParticipants).find(
          (user) => user.last_name === $event.target.value
        ) &&
        !this.editParticipant
      )
        this.warningAlert = true;
      this.warningMessage =
        'This last name already exists. Please verify if a person is actually a new participant';
      setTimeout(() => (this.warningAlert = false), 10000);
    },
    validatePhone($event) {
      this.v$.form.phone.$touch();
      if (
        Object.values(this.getParticipants).find(
          (user) => user.phone === $event.target.value
        ) &&
        !this.editParticipant
      )
        this.warningAlert = true;
      this.warningMessage =
        'This phone number already exists. Please verify if a person is actually a new paricipant';
      setTimeout(() => (this.warningAlert = false), 10000);
    },
  },
  watch: {
    selectedParticipant(newValue) {
      newValue ? this.onPopulateForm() : this.resetForm();
    },
  },
  computed: {
    ...mapGetters('participant', {
      getError: 'getError',
      getParticipants: 'getParticipants',
      getParticipant: 'getParticipant',
    }),
  },
};
</script>

<style lang="scss" scoped>
.add-participant-btn {
  color: #ffffff;
  caret-color: #ffffff;
  background-color: #607d8b !important;
  border-color: #607d8b;
}
</style>
