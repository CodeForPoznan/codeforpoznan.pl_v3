import { getMountWithProviders } from '../../../../../jest/utils';
import ParticipantsSearch from './ParticipantsSearch.vue';
import { expect, test, it } from 'vitest';

test('ParticipantsSearch component', () => {
  const mountWithProviders = getMountWithProviders();

  it('renders correctly', () => {
    const wrapper = mountWithProviders(ParticipantsSearch);

    expect(wrapper).toBeDefined();
  });
});
