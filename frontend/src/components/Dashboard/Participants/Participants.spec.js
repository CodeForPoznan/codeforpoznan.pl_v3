import { getMountWithProviders } from '../../../../jest/utils';
import Participants from './Participants';

describe('Participants component', () => {
  const mountWithProviders = getMountWithProviders();

  it('renders correctly', () => {
    const wrapper = mountWithProviders(Participants);

    expect(wrapper).toBeDefined();
  });
});
