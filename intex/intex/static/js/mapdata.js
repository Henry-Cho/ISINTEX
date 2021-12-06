var simplemaps_usmap_mapdata={
  main_settings: {
    //General settings
		width: "responsive", //or 'responsive'
    background_color: "#FFFFFF",
    background_transparent: "yes",
    popups: "detect",
    
		//State defaults
		state_description: "State description",
    state_color: "#88A4BC",
    state_hover_color: "#3B729F",
    state_url: "https://simplemaps.com",
    border_size: 1.5,
    border_color: "#ffffff",
    all_states_inactive: "no",
    all_states_zoomable: "no",
    
		//Location defaults
		location_description: "Location description",
    location_color: "#FF0067",
    location_opacity: 0.8,
    location_hover_opacity: 1,
    location_url: "",
    location_size: 25,
    location_type: "square",
    location_border_color: "#FFFFFF",
    location_border: 2,
    location_hover_border: 2.5,
    all_locations_inactive: "no",
    all_locations_hidden: "no",
    
		//Label defaults
		label_color: "#ffffff",
    label_hover_color: "#ffffff",
    label_size: 22,
    label_font: "Arial",
    hide_labels: "no",
   
		//Zoom settings
		manual_zoom: "yes",
    back_image: "no",
    arrow_box: "no",
    navigation_size: "40",
    navigation_color: "#f7f7f7",
    navigation_border_color: "#636363",
    initial_back: "no",
    initial_zoom: -1,
    initial_zoom_solo: "no",
    region_opacity: 1,
    region_hover_opacity: 0.6,
    zoom_out_incrementally: "yes",
    zoom_percentage: 0.99,
    zoom_time: 0.5,
    
		//Popup settings
		popup_color: "white",
    popup_opacity: 0.9,
    popup_shadow: 1,
    popup_corners: 5,
    popup_font: "12px/1.5 Verdana, Arial, Helvetica, sans-serif",
    popup_nocss: "no",
    
		//Advanced settings
		div: "map",
    auto_load: "yes",
    rotate: "0",
    url_new_tab: "yes",
    images_directory: "default",
    import_labels: "no",
    fade_time: 0.1,
    link_text: "View Website"
  },
  state_specific: {
    HI: {
      name: "Hawaii",
      description: "22 Prescribers",
      color: "default",
      hover_color: "#bc555e",
      url: "/searchstate/HI"
    },
    AK: {
      name: "Alaska",
      description: "7 Prescribers",
      color: "default",
      hover_color: "#d6ecef",
      url: "/searchstate/AK"
    },
    FL: {
      name: "Florida",
      description: "396 Prescribers",
      color: "default",
      hover_color: "#FFAE42",
      url: "/searchstate/FL",
      inactive: "no"
    },
    NH: {
      name: "New Hampshire",
      description: "25 Prescribers",
      color: "default",
      hover_color: "#987654",
      url: "/searchstate/NH"
    },
    VT: {
      name: "Vermont",
      description: "20 Prescribers",
      color: "default",
      hover_color: "#1B8E2D",
      url: "/searchstate/VT"
    },
    ME: {
      name: "Maine",
      description: "43 Prescribers",
      color: "default",
      hover_color: "#793734",
      url: "/searchstate/ME"
    },
    RI: {
      name: "Rhode Island",
      description: "26 Prescribers",
      color: "default",
      hover_color: "#793734",
      url: "/searchstate/RI"
    },
    NY: {
      name: "New York",
      description: "22 Prescribers",
      color: "default",
      hover_color: "#71797E",
      url: "/searchstate/HI"
    },
    PA: {
      name: "Pennsylvania",
      description: "314 Prescribers",
      color: "default",
      hover_color: "#793734",
      url: "/searchstate/PA"
    },
    NJ: {
      name: "New Jersey",
      description: "171 Prescribers",
      color: "default",
      hover_color: "#C0C0C0",
      url: "/searchstate/NJ"
    },
    DE: {
      name: "Delaware",
      description: "20 Prescribers",
      color: "default",
      hover_color: "#850102",
      url: "/searchstate/DE"
    },
    MD: {
      name: "Maryland",
      description: "101 Prescribers",
      color: "default",
      hover_color: "#cb4154",
      url: "/searchstate/MD"
    },
    VA: {
      name: "Virginia",
      description: "132 Prescribers",
      color: "default",
      hover_color: "#006400",
      url: "/searchstate/VA"
    },
    WV: {
      name: "West Virginia",
      description: "57 Prescribers",
      color: "default",
      hover_color: "#F0E68C",
      url: "/searchstate/WV"
    },
    OH: {
      name: "Ohio",
      description: "255 Prescribers",
      color: "default",
      hover_color: "#D2042D",
      url: "/searchstate/OH"
    },
    IN: {
      name: "Indiana",
      description: "133 Prescribers",
      color: "default",
      hover_color: "#FFAE42",
      url: "/searchstate/IN"
    },
    IL: {
      name: "Illinois",
      description: "239 Prescribers",
      color: "default",
      hover_color: "#71797E",
      url: "/searchstate/IL"
    },
    CT: {
      name: "Connecticut",
      description: "76 Prescribers",
      color: "default",
      hover_color: "#add8e6",
      url: "/searchstate/CT"
    },
    WI: {
      name: "Wisconsin",
      description: "128 Prescribers",
      color: "default",
      hover_color: "#6495ED",
      url: "/searchstate/WI"
    },
    NC: {
      name: "North Carolina",
      description: "227 Prescribers",
      color: "default",
      hover_color: "leaf green",
      url: "/searchstate/NC"
    },
    DC: {
      name: "District of Columbia",
      description: "17 Prescribers",
      color: "default",
      hover_color: "default",
      url: "/searchstate/DC"
    },
    MA: {
      name: "Massachusetts",
      description: "165 Prescribers",
      color: "default",
      hover_color: "#D65589",
      url: "/searchstate/MA"
    },
    TN: {
      name: "Tennessee",
      description: "148 Prescribers",
      color: "default",
      hover_color: "yellow",
      url: "/searchstate/TN"
    },
    AR: {
      name: "Arkansas",
      description: "60 Prescribers",
      color: "default",
      hover_color: "#013220",
      url: "/searchstate/AR"
    },
    MO: {
      name: "Missouri",
      description: "114 Prescribers",
      color: "default",
      hover_color: "#87ceeb",
      url: "/searchstate/MO"
    },
    GA: {
      name: "Georgia",
      description: "175 Prescribers",
      color: "default",
      hover_color: "#FFE5B4",
      url: "/searchstate/GA"
    },
    SC: {
      name: "South Carolina",
      description: "101 Prescribers",
      color: "default",
      hover_color: "#2D5A27",
      url: "/searchstate/SC"
    },
    KY: {
      name: "Kentucky",
      description: "111 Prescribers",
      color: "default",
      zoomable: "no",
      hover_color: "#006A6E",
      url: "/searchstate/KY"
    },
    AL: {
      name: "Alabama",
      description: "120 Prescribers",
      color: "default",
      hover_color: "000080",
      url: "/searchstate/AL"
    },
    LA: {
      name: "Louisiana",
      description: "100 Prescribers",
      color: "default",
      hover_color: "#d8bfd8",
      url: "/searchstate/LA"
    },
    MS: {
      name: "Mississippi",
      description: "46 Prescribers",
      color: "default",
      hover_color: "#5c4827",
      url: "/searchstate/MS"
    },
    IA: {
      name: "Iowa",
      description: "49 Prescribers",
      color: "default",
      hover_color: "#FBEC5D",
      url: "/searchstate/IA"
    },
    MN: {
      name: "Minnesota",
      description: "121 Prescribers",
      color: "default",
      hover_color: "#99FFFF",
      url: "/searchstate/MN"
    },
    OK: {
      name: "Oklahoma",
      description: "73 Prescribers",
      color: "default",
      hover_color: "#fcffa4",
      url: "/searchstate/OK"
    },
    TX: {
      name: "Texas",
      description: "349 Prescribers",
      color: "default",
      hover_color: "#C2B280",
      url: "/searchstate/TX"
    },
    NM: {
      name: "New Mexico",
      description: "39 Prescribers",
      color: "default",
      hover_color: "#FFD1DC",
      url: "/searchstate/NM"
    },
    KS: {
      name: "Kansas",
      description: "56 Prescribers",
      color: "default",
      hover_color: "#fffacd",
      url: "/searchstate/KS"
    },
    NE: {
      name: "Nebraska",
      description: "25 Prescribers",
      color: "default",
      hover_color: "#ffffbf",
      url: "/searchstate/NE"
    },
    SD: {
      name: "South Dakota",
      description: "28 Prescribers",
      color: "default",
      hover_color: "yellow",
      url: "/searchstate/SD"
    },
    ND: {
      name: "North Dakota",
      description: "19 Prescribers",
      color: "default",
      hover_color: "#FAFA33",
      url: "/searchstate/ND"
    },
    WY: {
      name: "Wyoming",
      description: "10 Prescribers",
      color: "default",
      hover_color: "#FBEC5D",
      url: "/searchstate/WY"
    },
    MT: {
      name: "Montana",
      description: "24 Prescribers",
      color: "default",
      hover_color: "#DD6E0F",
      url: "/searchstate/MT"
    },
    CO: {
      name: "Colorado",
      description: "76 Prescribers",
      color: "default",
      hover_color: "#FFA500",
      url: "/searchstate/CO"
    },
    UT: {
      name: "Utah",
      description: "32 Prescribers",
      color: "default",
      hover_color: "orange",
      url: "/searchstate/UT"
    },
    AZ: {
      name: "Arizona",
      description: "114 Prescribers",
      color: "default",
      hover_color: "#CC5500",
      url: "/searchstate/AZ"
    },
    NV: {
      name: "Nevada",
      description: "35 Prescribers",
      color: "default",
      hover_color: "#800000",
      url: "/searchstate/NV"
    },
    OR: {
      name: "Oregon",
      description: "74 Prescribers",
      color: "default",
      hover_color: "#9c51b6",
      url: "/searchstate/OR"
    },
    WA: {
      name: "Washington",
      description: "119 Prescribers",
      color: "default",
      hover_color: "#D2042D",
      url: "/searchstate/WA"
    },
    CA: {
      name: "California",
      description: "604 Prescribers",
      color: "default",
      hover_color: "#FF0000",
      url: "/searchstate/CA"
    },
    MI: {
      name: "Michigan",
      description: "224 Prescribers",
      color: "default",
      hover_color: "#87ceeb",
      url: "/searchstate/MI"
    },
    ID: {
      name: "Idaho",
      description: "30 Prescribers",
      color: "default",
      hover_color: "#FFFAFA",
      url: "/searchstate/ID"
    },
    GU: {
      name: "Guam",
      description: "46 Prescribers",
      color: "default",
      hover_color: "default",
      url: "/searchstate/GU",
      hide: "yes"
    },
    VI: {
      name: "Virgin Islands",
      description: "default",
      color: "default",
      hover_color: "default",
      url: "/searchstate/VI",
      hide: "yes"
    },
    PR: {
      name: "Puerto Rico",
      description: "default",
      color: "default",
      hover_color: "default",
      url: "/searchstate/PR",
      hide: "yes"
    },
    AS: {
      name: "American Samoa",
      description: "default",
      color: "default",
      hover_color: "default",
      url: "/searchstate/AS",
      hide: "yes"
    },
    MP: {
      name: "Northern Mariana Islands",
      description: "default",
      color: "default",
      hover_color: "default",
      url: "/searchstate/MP",
      hide: "yes"
    }
  },
  locations: {
    "0": {
      name: "New York",
      lat: 40.71,
      lng: -74,
      description: "default",
      color: "default",
      url: "default",
      type: "default",
      size: "default"
    },
    "1": {
      name: "Anchorage",
      lat: 61.2180556,
      lng: -149.9002778,
      color: "default",
      type: "circle"
    }
  },
  labels: {
    NH: {
      parent_id: "NH",
      x: "932",
      y: "183",
      pill: "yes",
      width: 45,
      display: "all"
    },
    VT: {
      parent_id: "VT",
      x: "883",
      y: "243",
      pill: "yes",
      width: 45,
      display: "all"
    },
    RI: {
      parent_id: "RI",
      x: "932",
      y: "273",
      pill: "yes",
      width: 45,
      display: "all"
    },
    NJ: {
      parent_id: "NJ",
      x: "883",
      y: "273",
      pill: "yes",
      width: 45,
      display: "all"
    },
    DE: {
      parent_id: "DE",
      x: "883",
      y: "303",
      pill: "yes",
      width: 45,
      display: "all"
    },
    MD: {
      parent_id: "MD",
      x: "932",
      y: "303",
      pill: "yes",
      width: 45,
      display: "all"
    },
    DC: {
      parent_id: "DC",
      x: "884",
      y: "332",
      pill: "yes",
      width: 45,
      display: "all"
    },
    MA: {
      parent_id: "MA",
      x: "932",
      y: "213",
      pill: "yes",
      width: 45,
      display: "all"
    },
    CT: {
      parent_id: "CT",
      x: "932",
      y: "243",
      pill: "yes",
      width: 45,
      display: "all"
    },
    HI: {
      parent_id: "HI",
      x: 305,
      y: 565,
      pill: "yes"
    },
    AK: {
      parent_id: "AK",
      x: "113",
      y: "495"
    },
    FL: {
      parent_id: "FL",
      x: "773",
      y: "510"
    },
    ME: {
      parent_id: "ME",
      x: "893",
      y: "85"
    },
    NY: {
      parent_id: "NY",
      x: "815",
      y: "158"
    },
    PA: {
      parent_id: "PA",
      x: "786",
      y: "210"
    },
    VA: {
      parent_id: "VA",
      x: "790",
      y: "282"
    },
    WV: {
      parent_id: "WV",
      x: "744",
      y: "270"
    },
    OH: {
      parent_id: "OH",
      x: "700",
      y: "240"
    },
    IN: {
      parent_id: "IN",
      x: "650",
      y: "250"
    },
    IL: {
      parent_id: "IL",
      x: "600",
      y: "250"
    },
    WI: {
      parent_id: "WI",
      x: "575",
      y: "155"
    },
    NC: {
      parent_id: "NC",
      x: "784",
      y: "326"
    },
    TN: {
      parent_id: "TN",
      x: "655",
      y: "340"
    },
    AR: {
      parent_id: "AR",
      x: "548",
      y: "368"
    },
    MO: {
      parent_id: "MO",
      x: "548",
      y: "293"
    },
    GA: {
      parent_id: "GA",
      x: "718",
      y: "405"
    },
    SC: {
      parent_id: "SC",
      x: "760",
      y: "371"
    },
    KY: {
      parent_id: "KY",
      x: "680",
      y: "300"
    },
    AL: {
      parent_id: "AL",
      x: "655",
      y: "405"
    },
    LA: {
      parent_id: "LA",
      x: "550",
      y: "435"
    },
    MS: {
      parent_id: "MS",
      x: "600",
      y: "405"
    },
    IA: {
      parent_id: "IA",
      x: "525",
      y: "210"
    },
    MN: {
      parent_id: "MN",
      x: "506",
      y: "124"
    },
    OK: {
      parent_id: "OK",
      x: "460",
      y: "360"
    },
    TX: {
      parent_id: "TX",
      x: "425",
      y: "435"
    },
    NM: {
      parent_id: "NM",
      x: "305",
      y: "365"
    },
    KS: {
      parent_id: "KS",
      x: "445",
      y: "290"
    },
    NE: {
      parent_id: "NE",
      x: "420",
      y: "225"
    },
    SD: {
      parent_id: "SD",
      x: "413",
      y: "160"
    },
    ND: {
      parent_id: "ND",
      x: "416",
      y: "96"
    },
    WY: {
      parent_id: "WY",
      x: "300",
      y: "180"
    },
    MT: {
      parent_id: "MT",
      x: "280",
      y: "95"
    },
    CO: {
      parent_id: "CO",
      x: "320",
      y: "275"
    },
    UT: {
      parent_id: "UT",
      x: "223",
      y: "260"
    },
    AZ: {
      parent_id: "AZ",
      x: "205",
      y: "360"
    },
    NV: {
      parent_id: "NV",
      x: "140",
      y: "235"
    },
    OR: {
      parent_id: "OR",
      x: "100",
      y: "120"
    },
    WA: {
      parent_id: "WA",
      x: "130",
      y: "55"
    },
    ID: {
      parent_id: "ID",
      x: "200",
      y: "150"
    },
    CA: {
      parent_id: "CA",
      x: "79",
      y: "285"
    },
    MI: {
      parent_id: "MI",
      x: "663",
      y: "185"
    },
    PR: {
      parent_id: "PR",
      x: "620",
      y: "545"
    },
    GU: {
      parent_id: "GU",
      x: "550",
      y: "540"
    },
    VI: {
      parent_id: "VI",
      x: "680",
      y: "519"
    },
    MP: {
      parent_id: "MP",
      x: "570",
      y: "575"
    },
    AS: {
      parent_id: "AS",
      x: "665",
      y: "580"
    }
  }
};