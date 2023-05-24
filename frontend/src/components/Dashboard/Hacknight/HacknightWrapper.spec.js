import HacknightWrapper from './HacknightWrapper';
import { getMountWithProviders } from '../../../../jest/utils';

describe('HacknightWrapper component', () => {
  const mountWithProviders = getMountWithProviders();

  it('renders correctly', () => {
    const wrapper = mountWithProviders(HacknightWrapper);

    expect(wrapper).toBeDefined();
  });
});
