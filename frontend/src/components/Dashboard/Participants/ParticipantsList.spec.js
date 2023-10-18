import { getMountWithProviders } from '../../../../jest/utils';
import ParticipantsList from './ParticipantsList.vue';
import { expect, test, it } from 'vitest';

test('ParticipantsList component', () => {
  const mountWithProviders = getMountWithProviders();

  it('renders correctly', () => {
    const wrapper = mountWithProviders(ParticipantsList);

    expect(wrapper).toBeDefined();
  });
});
