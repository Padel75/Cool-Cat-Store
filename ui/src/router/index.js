import { createRouter, createWebHashHistory } from "vue-router";
import Home from "@/views/Home";
import CustomerForm from "@/views/CustomerForm";
import ProductForm from "@/views/ProductForm";
import ProductPage from "@/views/ProductPage";
import SellerForm from "@/views/SellerForm";
import SellerPage from "@/views/SellerPage";

const routes = [
  {
    path: "/home",
    name: "Home",
    component: Home,
  },
  {
    path: "/customer",
    name: "CustomerForm",
    component: CustomerForm,
  },
  {
    path: "/product",
    name: "ProductForm",
    component: ProductForm,
  },
  {
    path: "/product/:id",
    name: "Product",
    component: ProductPage,
  },
  {
    path: "/seller",
    name: "SellerForm",
    component: SellerForm,
  },
  {
    path: "/seller/:id",
    name: "Seller",
    component: SellerPage,
  },

  {
    path: "/log-in",
    name: "Log-in",
    component: () => import("@/views/Log-in"),
  },
  {
    path: "/sign-up",
    name: "Sign-up",
    component: () => import("@/views/Sign-up"),
  },
];

export const router = createRouter({
  history: createWebHashHistory(),
  routes,
});
