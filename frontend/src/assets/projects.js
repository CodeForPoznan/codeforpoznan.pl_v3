const projects = [
  {
    badge: 'Zawieszony',
    description:
      'Portal Volontulo powstał dla ludzi i organizacji skupionych wokół idei pomocy innym poprzez udział we wolontariacie. Celem projektu jest pomoc we wzajemnym odnalezieniu się ludzi, którzy chcą realizować się jako wolontariusze/szki oraz organizacji i instytucji, które takich osób poszukują. Podział na strefę "Wolontariusza" oraz "Strefę organizacji i instytucji" umożliwa użytkownikom zwinną nawigację na stronie.',
    githubLink: 'https://github.com/CodeForPoznan/volontulo',
    imageAdress: require('@/assets/images/volontulo.png'),
    licenseName: 'MIT',
    licensePage: 'https://pl.wikipedia.org/wiki/Licencja_MIT',
    name: 'Volontulo',
    partner: [],
    stack: [
      {
        type: 'Frontend',
        name: 'Angular',
        version: '2.0',
        documentation: 'https://angular.io/'
      },
      {
        type: 'Backend',
        name: 'Django',
        version: '2.2',
        documentation: 'https://docs.djangoproject.com/pl/2.2/'
      }
    ],
    website: ''
  },
  {
    badge: 'Aktywny',
    description:
      'W wyniku współpracy z Polską Akcją Humanitarną stworzyliśmy aplikację pomagającą w logistycznych procesach akcji humanitarnych w różnych częściach globu. Aktualnie aplikacja służąca rejestracji i ewidencji przejazdów jest wykorzystywana podczas akcji humanitarnych na Ukrainie, w Sudanie Południowym, Jemenie oraz Somalii. Aplikacja pozwala także na eksport zebranych danych w celu ewidencji kosztów dla danej akcji humanitarnej. Dzięku temu możemy zoptymalizować proces i zmniejszyć nakład papierkowej pracy biurowej.',
    githubLink: 'https://github.com/CodeForPoznan/pah-fm',
    imageAdress: require('@/assets/images/PAH.png'),
    license: 'MIT',
    licensePage: 'https://github.com/CodeForPoznan/pah-fm/pull/401/files',
    name: 'Fleet Manager',
    partner: [
      {
        name: 'Polska Akcja Humanitarna',
        link: 'https://www.pah.org.pl/'
      }
    ],
    stack: [
      {
        type: 'Frontend',
        name: 'Vue.js',
        version: '2.5',
        documentation: 'https://vuejs.org/v2/guide/'
      },
      {
        type: 'Backend',
        name: 'Django',
        version: '2.2',
        documentation: 'https://docs.djangoproject.com/pl/2.2/'
      }
    ],
    website: 'https://github.com/CodeForPoznan/pah-fm#readme'
  },
  {
    badge: 'Aktywny',
    description:
      'Aplikacja Alinka powstała w celu optymalizacji codziennej pracy w poradniach psychologiczno-pedagogicznych. Jako byli pracownicy takiej poradni doskonale rozumiemy jakiego nakładu pracy wymaga wydanie orzeczenia czy sporządzenie protokołu z posiedzenia komisji. Aplikacja Alinka jest odpowiedzią na trudności, z jakimi spotykają się w codziennej pracy pracownicy administracji poradni. Nazwa aplikacji: „Alinka” to imię prawdziwej osoby, która musi wykonywać tę nudną, ale bardzo ważną pracę. Mamy nadzieję, że któregoś dnia ta aplikacja pomoże w jej pracy :).',
    githubLink: 'https://github.com/CodeForPoznan/alinka-electron',
    imageAdress: require('@/assets/images/alinka.png'),
    license: 'MIT',
    licensePage:
      'https://github.com/CodeForPoznan/alinka-electron/blob/master/LICENSE',
    name: 'Alinka',
    partner: [
      {
        name: 'Poradnia Psychologiczno-Pedagogiczna w Grodzisku Wielkopolskim',
        link: 'http://www.grodziskwlkp.naszaporadnia.com/aktualnosci'
      },
      {
        name: 'Poradnia Pscyhologiczno-Pedagogiczna we Wrześni',
        link: 'https://ppp-wrzesnia.pl/'
      }
    ],
    stack: [
      {
        type: 'Frontend',
        name: 'React',
        version: '16.8',
        documentation: 'https://pl.reactjs.org/docs/getting-started.html'
      },
      {
        type: 'Backend',
        name: 'Electron',
        version: '3.0',
        documentation: 'https://www.electronjs.org/docs'
      },
      {
        type: 'Database',
        name: 'SQLite',
        version: '3.0',
        documentation: 'https://www.sqlite.org/docs.html'
      }
    ],
    website: 'https://alinka.io'
  },
  {
    badge: 'Wspierany',
    description:
      'Bank Empatii to projekt strony Patrycji Krawczyk, która zmaga się z białaczką limfoblastyczną i chce znaleźć dawcę komórek macierzystach o podobnym do Patrycji kodzie genetycznym. Trzy główne panele "Historia Patrycji", "Jak wygląda badanie? oraz "Gdzie się zgłosić?" kierują użytkowników strony do uzyskania informacji na temat jak zostać dawcą szpiku oraz czym jest Rejestr Dawców. Na stronie znajduje się mapa Polski z umiejscowieniem punktów poboru krwi.',
    githubLink: 'https://github.com/CodeForPoznan/empatia',
    imageAdress: require('@/assets/images/bank_empatii.png'),
    license: 'MIT',
    licensePage: 'https://github.com/CodeForPoznan/empatia/blob/master/LICENSE',
    name: 'Bank Empatii',
    partner: [],
    stack: [],
    website: 'http://bankempatii.pl/'
  },
  {
    badge: 'Zawieszony',
    description:
      'Oryginalny Streetmix jest dziełem Code for America, które w 2013 roku podczas hacknightu postanowiło stworzyć narzędzie, które pomoże miejskim planistom w przedstawianiu koncepcji ich planu na rewitalizacje miejskiej przestrzeni. Najczęstszym rozwiązaniem po jakie sięgają planiści jest wykonanie makiet z papieru, które zwizualizują krajobraz. Tworząc internetową wersję tego działania, planiści mogą dotrzeć do szerszego grona odbiorców niż podczas samych spotkań, a także pozwolić członkom społeczności na dzielenie się i remiksowanie swoich dzieł. Jest to jeden z pierwszych naszych projektów, które mieliśmy przyjemność przetłumaczyć tak, aby można było wykorzystać te rozwiązanie na polskim gruncie.',
    githubLink: 'https://github.com/CodeForPoznan/streetmix',
    imageAdress: require('@/assets/images/streetmix.png'),
    license: 'BSD 3-Clause',
    licensePage:
      'https://github.com/CodeForPoznan/streetmix/blob/master/LICENSE.md',
    name: 'StreetMix',
    partner: [],
    stack: [
      {
        type: 'Frontend',
        name: 'React',
        version: '16.2',
        documentation: 'https://pl.reactjs.org/docs/getting-started.html'
      }
    ],
    website: 'https://streetmix.net'
  },
  {
    badge: 'Zawieszony',
    description:
      'Wysadźulice.pl jest przykładem aplikacji umożliwiającej zaplanowanie czy zaprojektowanie przestrzeni, która nas otacza. Każdy użytkownik apliakcji ma dzięki niej realny wpływ na wygląd i funkcjonalność ulicy, przy której mieszka czy parku do którego chodzi. Wystraczy zrobić zdjęcie lub wgrać obraz z Google Street View, następnie dodać elementy w postaci: kwiatów, krzewów, drzew czy ławki. Tak przygotowana wizualizacja może posłużyć na konsultacjach z władzami miast czy gmin.',
    githubLink: 'https://github.com/CodeForPoznan/wysadzulice.pl',
    imageAdress: require('@/assets/images/wysadz_ulice.png'),
    license: 'MIT',
    licensePage: 'https://pl.wikipedia.org/wiki/Licencja_MIT',
    name: 'Wysadź ulicę',
    partner: [],
    stack: [],
    website: ''
  },
  {
    badge: 'Aktywny',
    description:
      'Jest to trzecia wersja strony internetowej naszej organizacji. To pokazuje, że jako stowarzyszenie ciągle się rozwijamy i potrzebujemy nowych narzędzi i funkcjonalności do codziennej pracy. Aktualna forma strony jest wynikiem ponad 3 lat działalności jako Code for Poznań.',
    githubLink: 'https://github.com/CodeForPoznan/codeforpoznan.pl_v3',
    imageAdress: require('@/assets/images/StronaSpolecznosci.png'),
    license: 'MIT',
    licensePage:
      'https://github.com/CodeForPoznan/codeforpoznan.pl_v3/blob/master/LICENSE',
    name: 'Platforma społeczności',
    partner: [],
    stack: [
      {
        type: 'Frontend',
        name: 'Vue.js',
        version: '2.6',
        documentation: 'https://vuejs.org/v2/guide/'
      },
      {
        type: 'Frontend',
        name: 'Vuetify',
        version: '2.0',
        documentation: 'https://vuetifyjs.com/en/getting-started/quick-start/'
      },
      {
        type: 'Frontend',
        name: 'Vuex',
        version: '3.0',
        documentation: 'https://vuex.vuejs.org/guide/'
      },
      {
        type: 'Backend',
        name: 'Flask',
        version: '1.0',
        documentation: 'https://flask.palletsprojects.com/en/1.0.x/'
      }
    ],
    website: 'https://dev.codeforpoznan.pl/'
  },
  {
    badge: 'Aktywny',
    description:
      'Watchdog Polska od 2003 roku stoi na straży prawa do informacji. Rozumiane jest ono nie tylko jako warunek funkcjonowania dobrego państwa, ale przede wszystkim jako jedno z praw człowieka, które chroni ludzką godność, daje wolność wyrażania opinii i zabezpiecza przed nadużyciami władzy. W ciągu 17 lat swojej działalności Sieć Obywatelska Watchdog Polska uczestniczyła w około 1122 sprawach sądowych dotyczących prawa do informacji. Niektóre z nich miały przełomowe znaczenie dla społeczeństwa. Razem współtworzymy system służący do usprawnienia obiegu dokumentów Stowarzyszenia, w szczególności korespondencji sądowej.',
    githubLink: 'https://github.com/watchdogpolska/small_eod',
    imageAdress: require('@/assets/images/watchdog.png'),
    license: 'MIT',
    licensePage: 'https://github.com/CodeForPoznan/small_eod/blob/dev/LICENSE',
    name: 'EOD',
    partner: [
      {
        name: 'Watchdog Polska',
        link: 'https://siecobywatelska.pl/'
      }
    ],
    stack: [
      {
        name: 'React.js',
        documentation: 'https://reactjs.org/docs/getting-started.html'
      },
      {
        name: 'PostgresSQL',
        documentation: 'https://www.postgresql.org/'
      },
      {
        name: 'Django',
        documentation: 'https://docs.djangoproject.com/en/3.2/'
      },
      {
        name: 'Minio',
        documentation: 'https://docs.min.io/'
      }
    ],
    website: 'dev.small-eod.siecobywatelska.pl'
  }
];

const badgeOrder = {
  Aktywny: 1,
  Wspierany: 2,
  Zawieszony: 3
};

let sortedProjects = [...projects].sort(
  (a, b) => badgeOrder[a.badge] - badgeOrder[b.badge]
);

export default sortedProjects;
