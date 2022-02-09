import { getMountWithProviders } from '../../../jest/utils';
import Login from './Login';

describe('Login component', () => {
  const mountWithProviders = getMountWithProviders();

  it('renders correctly', () => {
    const wrapper = mountWithProviders(Login);

    expect(wrapper).toBeDefined();
  });
});
