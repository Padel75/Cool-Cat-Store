import { createRouter, createWebHashHistory } from "vue-router";
import Home from "@/views/Home";
import ProductPage from "@/views/ProductPage";
import LogIn from "@/views/LogIn.vue";
import SignUpCustomer from "@/views/SignUpCustomer.vue";
import SignUpSeller from "@/views/SignUpSeller";
import SellerPage from "@/views/SellerPage";

const routes = [
  {
    path: "/home",
    name: "Home",
    component: Home,
  },
  {
    path: "/signup/customer",
    name: "SignUpCustomer",
    component: SignUpCustomer,
  },
  {
    path: "/product/:id",
    name: "Product",
    component: ProductPage,
  },
  {
    path: "/signup/seller",
    name: "SignUpSeller",
    component: SignUpSeller,
  },
  {
    path: "/seller", //seller/:id removed until seller page aviable in backend
    name: "Seller",
    component: SellerPage,
  },

  {
    path: "/login",
    name: "LogIn",
    component: LogIn,
  },
  {
    path: "/signup",
    name: "SignUp",
    component: () => import("@/views/SignUp.vue"),
  },
];

export const router = createRouter({
  history: createWebHashHistory(),
  routes,
});
