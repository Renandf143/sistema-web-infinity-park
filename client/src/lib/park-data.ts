import { 
  ParkArea, 
  AttractionCategory, 
  Attraction, 
  Restaurant, 
  Event, 
  TicketType,
  ParkService 
} from "@shared/schema";

// Park Areas/Zones
export const parkAreas: ParkArea[] = [
  {
    id: 1,
    name: "Adventureland",
    description: "Uma terra de aventuras exóticas e mistérios antigos",
    imageUrl: "https://images.unsplash.com/photo-1544474333-d2833eb5b8cc?w=800",
    mapCoordinates: { x: 100, y: 150, width: 300, height: 200 },
    theme: "adventureland",
    color: "#8B4513"
  },
  {
    id: 2,
    name: "Fantasyland",
    description: "O reino mágico dos contos de fadas",
    imageUrl: "https://images.unsplash.com/photo-1518611012118-696072aa579a?w=800",
    mapCoordinates: { x: 450, y: 100, width: 350, height: 250 },
    theme: "fantasyland",
    color: "#9370DB"
  },
  {
    id: 3,
    name: "Tomorrowland",
    description: "O futuro está aqui com tecnologia e inovação",
    imageUrl: "https://images.unsplash.com/photo-1562113530-57ba23cea03c?w=800",
    mapCoordinates: { x: 200, y: 400, width: 300, height: 200 },
    theme: "tomorrowland",
    color: "#4169E1"
  },
  {
    id: 4,
    name: "Frontierland",
    description: "O selvagem oeste americano ganha vida",
    imageUrl: "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800",
    mapCoordinates: { x: 550, y: 400, width: 250, height: 200 },
    theme: "frontierland",
    color: "#D2691E"
  }
];

// Attraction Categories
export const attractionCategories: AttractionCategory[] = [
  {
    id: 1,
    name: "Montanha-Russa",
    description: "Emoção e adrenalina em alta velocidade",
    icon: "zap",
    color: "#DC2626"
  },
  {
    id: 2,
    name: "Aventura Aquática",
    description: "Diversão refrescante com água",
    icon: "waves",
    color: "#2563EB"
  },
  {
    id: 3,
    name: "Família",
    description: "Diversão para toda a família",
    icon: "users",
    color: "#16A34A"
  },
  {
    id: 4,
    name: "Radical",
    description: "Para os mais corajosos",
    icon: "flame",
    color: "#EA580C"
  },
  {
    id: 5,
    name: "Infantil",
    description: "Perfeito para os pequenos",
    icon: "baby",
    color: "#7C3AED"
  }
];

// Attractions with real theme park inspiration
export const attractions: Attraction[] = [
  // Adventureland
  {
    id: 1,
    name: "Piratas do Caribe",
    description: "Navegue pelos mares perigosos e descubra tesouros escondidos nesta aventura épica pelos sete mares. Enfrente piratas, tempestades e criaturas marinhas misteriosas.",
    shortDescription: "Aventura naval épica com piratas e tesouros",
    categoryId: 3,
    areaId: 1,
    imageUrl: "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=800",
    galleryImages: [
      "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=800",
      "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=800",
      "https://images.unsplash.com/photo-1520637836862-4d197d17c27a?w=800"
    ],
    mapCoordinates: { x: 150, y: 180 },
    minHeight: 100,
    maxHeight: null,
    duration: 8,
    capacity: 24,
    thrillLevel: 2,
    isActive: true,
    waitTime: 35,
    fastPassAvailable: true,
    wheelchairAccessible: true,
    hearingImpairedAccess: true,
    visuallyImpairedAccess: false,
    rating: 4.8,
    reviewCount: 2847,
    openTime: "09:00",
    closeTime: "22:00",
    createdAt: new Date(),
    updatedAt: new Date()
  },
  {
    id: 2,
    name: "Jungle Cruise",
    description: "Uma jornada hilária pelos rios mais perigosos do mundo com nossos guias especializados em piadas ruins e aventuras incríveis.",
    shortDescription: "Cruzeiro cômico pela selva selvagem",
    categoryId: 3,
    areaId: 1,
    imageUrl: "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=800",
    galleryImages: [
      "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=800",
      "https://images.unsplash.com/photo-1544474333-d2833eb5b8cc?w=800"
    ],
    mapCoordinates: { x: 200, y: 220 },
    minHeight: 80,
    maxHeight: null,
    duration: 10,
    capacity: 32,
    thrillLevel: 1,
    isActive: true,
    waitTime: 25,
    fastPassAvailable: false,
    wheelchairAccessible: true,
    hearingImpairedAccess: true,
    visuallyImpairedAccess: true,
    rating: 4.5,
    reviewCount: 1923,
    openTime: "09:00",
    closeTime: "22:00",
    createdAt: new Date(),
    updatedAt: new Date()
  },

  // Fantasyland
  {
    id: 3,
    name: "Space Mountain",
    description: "Voe através das galáxias em completa escuridão nesta montanha-russa espacial única. Uma experiência inesquecível nas estrelas!",
    shortDescription: "Montanha-russa espacial no escuro",
    categoryId: 1,
    areaId: 2,
    imageUrl: "https://images.unsplash.com/photo-1562113530-57ba23cea03c?w=800",
    galleryImages: [
      "https://images.unsplash.com/photo-1562113530-57ba23cea03c?w=800",
      "https://images.unsplash.com/photo-1446776653964-20c1d3a81b06?w=800"
    ],
    mapCoordinates: { x: 500, y: 150 },
    minHeight: 120,
    maxHeight: null,
    duration: 3,
    capacity: 12,
    thrillLevel: 4,
    isActive: true,
    waitTime: 65,
    fastPassAvailable: true,
    wheelchairAccessible: false,
    hearingImpairedAccess: true,
    visuallyImpairedAccess: false,
    rating: 4.9,
    reviewCount: 4521,
    openTime: "09:00",
    closeTime: "23:00",
    createdAt: new Date(),
    updatedAt: new Date()
  },
  {
    id: 4,
    name: "Castelo da Princesa",
    description: "Explore o majestoso castelo e conheça suas princesas favoritas em um passeio mágico através dos contos de fadas mais amados.",
    shortDescription: "Tour mágico pelo castelo encantado",
    categoryId: 5,
    areaId: 2,
    imageUrl: "https://images.unsplash.com/photo-1518611012118-696072aa579a?w=800",
    galleryImages: [
      "https://images.unsplash.com/photo-1518611012118-696072aa579a?w=800",
      "https://images.unsplash.com/photo-1571003123394-b7dde9b8f395?w=800"
    ],
    mapCoordinates: { x: 600, y: 200 },
    minHeight: 0,
    maxHeight: null,
    duration: 12,
    capacity: 20,
    thrillLevel: 1,
    isActive: true,
    waitTime: 40,
    fastPassAvailable: true,
    wheelchairAccessible: true,
    hearingImpairedAccess: true,
    visuallyImpairedAccess: true,
    rating: 4.7,
    reviewCount: 3264,
    openTime: "09:00",
    closeTime: "22:00",
    createdAt: new Date(),
    updatedAt: new Date()
  },

  // Tomorrowland
  {
    id: 5,
    name: "Hyperspace Mountain",
    description: "Uma experiência de realidade virtual revolucionária que te transporta para outros planetas em uma jornada intergaláctica emocionante.",
    shortDescription: "Aventura VR intergaláctica",
    categoryId: 1,
    areaId: 3,
    imageUrl: "https://images.unsplash.com/photo-1446776653964-20c1d3a81b06?w=800",
    galleryImages: [
      "https://images.unsplash.com/photo-1446776653964-20c1d3a81b06?w=800",
      "https://images.unsplash.com/photo-1562113530-57ba23cea03c?w=800"
    ],
    mapCoordinates: { x: 300, y: 450 },
    minHeight: 130,
    maxHeight: null,
    duration: 4,
    capacity: 16,
    thrillLevel: 5,
    isActive: true,
    waitTime: 85,
    fastPassAvailable: true,
    wheelchairAccessible: false,
    hearingImpairedAccess: false,
    visuallyImpairedAccess: false,
    rating: 4.9,
    reviewCount: 5847,
    openTime: "10:00",
    closeTime: "23:00",
    createdAt: new Date(),
    updatedAt: new Date()
  },

  // Frontierland
  {
    id: 6,
    name: "Thunder Mountain Railroad",
    description: "Viaje de trem pelas montanhas do velho oeste em uma aventura cheia de surpresas, cavernas misteriosas e paisagens deslumbrantes.",
    shortDescription: "Trem da montanha do velho oeste",
    categoryId: 1,
    areaId: 4,
    imageUrl: "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800",
    galleryImages: [
      "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800",
      "https://images.unsplash.com/photo-1552074284-5e88ef1aef18?w=800"
    ],
    mapCoordinates: { x: 650, y: 480 },
    minHeight: 110,
    maxHeight: null,
    duration: 6,
    capacity: 32,
    thrillLevel: 3,
    isActive: true,
    waitTime: 45,
    fastPassAvailable: true,
    wheelchairAccessible: false,
    hearingImpairedAccess: true,
    visuallyImpairedAccess: false,
    rating: 4.6,
    reviewCount: 2946,
    openTime: "09:00",
    closeTime: "22:00",
    createdAt: new Date(),
    updatedAt: new Date()
  },

  // Water attractions
  {
    id: 7,
    name: "Splash Mountain",
    description: "Prepare-se para se molhar! Uma descida emocionante de 20 metros em uma aventura aquática inesquecível com direito a fotos no final.",
    shortDescription: "Descida aquática radical",
    categoryId: 2,
    areaId: 1,
    imageUrl: "https://images.unsplash.com/photo-1558618047-3c8c76ca7d13?w=800",
    galleryImages: [
      "https://images.unsplash.com/photo-1558618047-3c8c76ca7d13?w=800",
      "https://images.unsplash.com/photo-1575550959106-5a7defe28b56?w=800"
    ],
    mapCoordinates: { x: 350, y: 280 },
    minHeight: 120,
    maxHeight: null,
    duration: 5,
    capacity: 8,
    thrillLevel: 4,
    isActive: true,
    waitTime: 55,
    fastPassAvailable: true,
    wheelchairAccessible: false,
    hearingImpairedAccess: true,
    visuallyImpairedAccess: false,
    rating: 4.8,
    reviewCount: 3785,
    openTime: "10:00",
    closeTime: "21:00",
    createdAt: new Date(),
    updatedAt: new Date()
  },

  {
    id: 8,
    name: "Carrousel Mágico",
    description: "Um carrossel clássico com cavalos mágicos que sobem e descem ao som de músicas encantadoras. Perfeito para toda a família!",
    shortDescription: "Carrossel clássico familiar",
    categoryId: 5,
    areaId: 2,
    imageUrl: "https://images.unsplash.com/photo-1453614946848-5aa2c4537d7c?w=800",
    galleryImages: [
      "https://images.unsplash.com/photo-1453614946848-5aa2c4537d7c?w=800",
      "https://images.unsplash.com/photo-1460904577954-8fadb262612c?w=800"
    ],
    mapCoordinates: { x: 550, y: 180 },
    minHeight: 0,
    maxHeight: null,
    duration: 3,
    capacity: 40,
    thrillLevel: 1,
    isActive: true,
    waitTime: 15,
    fastPassAvailable: false,
    wheelchairAccessible: true,
    hearingImpairedAccess: true,
    visuallyImpairedAccess: true,
    rating: 4.3,
    reviewCount: 1856,
    openTime: "09:00",
    closeTime: "22:00",
    createdAt: new Date(),
    updatedAt: new Date()
  }
];

// Restaurants
export const restaurants: Restaurant[] = [
  {
    id: 1,
    name: "Pirates Tavern",
    description: "Restaurante temático pirata com pratos do mar e ambiente de taverna autêntica",
    areaId: 1,
    imageUrl: "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=800",
    mapCoordinates: { x: 180, y: 320 },
    cuisine: "frutos-do-mar",
    priceRange: 3,
    rating: 4.5,
    reviewCount: 892,
    isActive: true,
    openTime: "11:00",
    closeTime: "22:00"
  },
  {
    id: 2,
    name: "Royal Feast",
    description: "Experiência gastronômica real com princesas e pratos refinados",
    areaId: 2,
    imageUrl: "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=800",
    mapCoordinates: { x: 580, y: 220 },
    cuisine: "internacional",
    priceRange: 4,
    rating: 4.8,
    reviewCount: 1247,
    isActive: true,
    openTime: "12:00",
    closeTime: "21:00"
  },
  {
    id: 3,
    name: "Cosmic Diner",
    description: "Restaurante futurista com comida molecular e experiência interativa",
    areaId: 3,
    imageUrl: "https://images.unsplash.com/photo-1466978913421-dad2ebd01d17?w=800",
    mapCoordinates: { x: 280, y: 520 },
    cuisine: "fusion",
    priceRange: 3,
    rating: 4.4,
    reviewCount: 634,
    isActive: true,
    openTime: "11:30",
    closeTime: "22:30"
  }
];

// Events and Shows
export const events: Event[] = [
  {
    id: 1,
    name: "Parada dos Sonhos",
    description: "Espetacular parada com carros alegóricos, personagens e muita música!",
    areaId: 2,
    imageUrl: "https://images.unsplash.com/photo-1520637736862-4d197d17c27a?w=800",
    mapCoordinates: { x: 400, y: 300 },
    eventType: "parade",
    duration: 45,
    capacity: 5000,
    isRecurring: true,
    showTimes: ["15:00", "19:00"],
    startDate: new Date(),
    endDate: null,
    ticketRequired: false,
    isActive: true
  },
  {
    id: 2,
    name: "Show de Fogos Infinito",
    description: "Espetáculo noturno com fogos de artifício, projeções e música",
    areaId: 2,
    imageUrl: "https://images.unsplash.com/photo-1531306728370-e2ebd9d7bb99?w=800",
    mapCoordinates: { x: 450, y: 250 },
    eventType: "show",
    duration: 20,
    capacity: 10000,
    isRecurring: true,
    showTimes: ["21:30"],
    startDate: new Date(),
    endDate: null,
    ticketRequired: false,
    isActive: true
  }
];

// Ticket Types
export const ticketTypes: TicketType[] = [
  {
    id: 1,
    name: "Ingresso 1 Dia",
    description: "Acesso completo ao parque por um dia",
    price: "199.90",
    type: "single-day",
    validDays: 1,
    includes: ["park-access", "shows", "parades"],
    isActive: true
  },
  {
    id: 2,
    name: "Ingresso 2 Dias",
    description: "Acesso completo ao parque por dois dias consecutivos",
    price: "349.90",
    type: "multi-day",
    validDays: 2,
    includes: ["park-access", "shows", "parades"],
    isActive: true
  },
  {
    id: 3,
    name: "Fast Pass",
    description: "Pule as filas nas principais atrações",
    price: "89.90",
    type: "fast-pass",
    validDays: 1,
    includes: ["priority-access"],
    isActive: true
  },
  {
    id: 4,
    name: "Passe Anual",
    description: "Acesso ilimitado ao parque por um ano inteiro",
    price: "1299.90",
    type: "season-pass",
    validDays: 365,
    includes: ["park-access", "shows", "parades", "parking", "discounts"],
    isActive: true
  }
];

// Park Services
export const parkServices: ParkService[] = [
  {
    id: 1,
    name: "Banheiros Adventureland",
    type: "restroom",
    areaId: 1,
    mapCoordinates: { x: 130, y: 280 },
    icon: "bath",
    isActive: true
  },
  {
    id: 2,
    name: "Primeiros Socorros Central",
    type: "first-aid",
    areaId: 2,
    mapCoordinates: { x: 500, y: 300 },
    icon: "heart-pulse",
    isActive: true
  },
  {
    id: 3,
    name: "Caixa Eletrônico Tomorrowland",
    type: "atm",
    areaId: 3,
    mapCoordinates: { x: 250, y: 480 },
    icon: "credit-card",
    isActive: true
  },
  {
    id: 4,
    name: "Loja de Souvenirs Fantasyland",
    type: "gift-shop",
    areaId: 2,
    mapCoordinates: { x: 620, y: 280 },
    icon: "gift",
    isActive: true
  },
  {
    id: 5,
    name: "Ponto Fotográfico Castelo",
    type: "photo-spot",
    areaId: 2,
    mapCoordinates: { x: 600, y: 200 },
    icon: "camera",
    isActive: true
  }
];