# Frontend automated testing

## Unit tests

### Run unit tests locally

- open terminal in `codeforpoznan.pl_v3/frontend` directory,
- (skip this, if you already have the dependencies installed) run `npm i` to make sure that you have all the dependencies for test runner installed,
- run one of following commands:
  - `npm test` if you want to run all of existing tests once - this is mostly used at the end of development process, to see that your changes do not break anything in other places. It's also a command that will be executed upon your changes when you push your code to Github, so if it fails you won't be able to merge your changes until the tests are fixed.
  - `npm run test:watch` if you want to see immediate feedback on the changes you are making during the development. Usually this command is used when working on unit tests as it will only run tests relevant to your changes as well as trigger re-run on every file change, so the feedback is very quick. Once you run this command, you will see some additionall options to run for example 'only failed tests' or 'all tests', which might also become handy during development.
  - `npm test path_to_file` if you want to run a single test file once - just paste relative path to the file in place of `path_to_file`, for example `npm run test src/components/HomePage/ContactUs/ContactUs.spec.js`.
  - `npm run test:watch path_to_file` if you want to run a single test file in watch mode - just paste relative path to the file in place of `path_to_file`, for example `npm run test src/components/HomePage/ContactUs/ContactUs.spec.js`.

### Test output

Test output should contain three sections:

- output of each single test - shows additional info in case some test fails, you can find the exact error that needs to be fixed in here,
- table with test coverage - shows which parts of our codebase are covered by unit test and which of them still need some work in this area (it's ok if not everything is green here but we should aim for it),
- test summary - shows how many tests were ran, how many passed and how many failed.

### Setup and configuration

Unit tests in `frontend` directory are implemented with [Jest.io](https://jestjs.io/) as test runner and [Vue Test Utils](https://vue-test-utils.vuejs.org/) as components renderer. You will find most of the relevent documentation there.

Tests configuration is done in:

- `frontend/jest.config.js` - this is where the configuration of test runner is kept, you can find all of the options documentation [here](https://jestjs.io/docs/configuration).
- `frontend/jest/jest.setup.js` - this is the file, which is executed to prepare an environment for each test run.
- `frontend/jest/utils.js` - contains custom `mount` methods, that are a workaround for the common issues with testing components using `Vuetify` and `Vuex`. Each of them creates a local Vue instance. Explanations of the issues are linked inside the file in comments.

Other tooling:

- `.travis.yml` is where the command for tests running in Github pipeline is kept,
- `.gitignore` is where the `frontend/coverage/` directory is ignored so that it won't be commited to the codebase,
- `frontend/.eslintrc.json` is where the lint configuration for test files is kept.

### Writting unit tests

#### File structure and naming

When adding new components or tests please follow the pattern:

- _Folder_ ComponentName
  - _Component_ ComponentName.vue
  - _Test_ ComponentName.spec.js

It's OK to have this structure nested even a couple times if the component is combined of several other components.

#### Test file

- Test file should start with the `import` statements, just as any other JS file. For basic scenario, you will need to import the component that you will be testing and a function that will render it. Depending on the complexity of your component, you will need one of the following:
  - `import { shallowMount } from '@vue/test-utils';` for the components that do not depend on Vuetify or Vuex;
  - `import { getMountWithProviders } from '../jest/utils';` for components depending on both Vue and Vuex;
  - `import { getMountWithVue } from '../jest/utils';` for components depending on Vue;
  - `import { getMountWithVuex } from '../jest/utils';` for components depending on Vuex;
    Note, that functions from `jest/utils` need to be called on main test level and they return the actual mount methods, that can be later used for rendering the components. Here is an example:

```javascript
import { getMountWithProviders } from '../../../jest/utils';
import HomePage from './HomePage';

describe('HomePage component', () => {
  const mountWithProviders = getMountWithProviders();

  it('renders correctly', () => {
    const wrapper = mountWithProviders(HomePage);

    expect(wrapper).toBeDefined();
  });
});
```

- The actual test is enclosed in `describe` function, which comes from Jest. It takes two arguments:
  - string which will be treated as a title for your test,
  - callback function, in which you write your test cases for test runner to execute.
- Test cases are enclosed in `it` function that also comes from Jest and takes two arguments:
  - string which will be treated as a title for your test case,
  - callback function, in which you should mount the component and `expect` something to happen.
- `Expect` function comes from Jest as well and has some methods implemented that allow to make assertions, you can look for available options [here](https://jestjs.io/docs/expect).

#### Tips

- Although nesting `describes` is possible, try to avoid it and keep the test structure as flat as possible, so other developers can easily understand what's going on.
- Having multiple `expect` statements in one `it` is not a bad thing, as long as you do not modify rendered component in between.
- All concepts described here are common paterns and you will find plenty of information by just googling it, if you need more context.
