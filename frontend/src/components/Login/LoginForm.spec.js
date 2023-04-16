import { getMountWithProviders } from '../../../jest/utils';
import LoginForm from './LoginForm';

describe('LoginForm component', () => {
  const mountWithProviders = getMountWithProviders();

  it('renders correctly', () => {
    const wrapper = mountWithProviders(LoginForm);

    expect(wrapper).toBeDefined();
  });
});
