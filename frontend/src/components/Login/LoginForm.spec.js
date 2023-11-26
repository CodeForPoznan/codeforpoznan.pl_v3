import { getMountWithProviders } from '../../../jest/utils';
import LoginForm from './LoginForm.vue';
import { expect, test, it } from 'vitest';

test('LoginForm component', () => {
  const mountWithProviders = getMountWithProviders();

  it('renders correctly', () => {
    const wrapper = mountWithProviders(LoginForm);

    expect(wrapper).toBeDefined();
  });
});
