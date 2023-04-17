import { createRouter, createWebHashHistory } from "vue-router";
import Home from "@/views/Home";
import CustomerForm from "@/views/CustomerForm";
import PaymentForm from "@/views/PaymentForm.vue";
import ProductForm from "@/views/ProductForm";
import ProductPage from "@/views/ProductPage";
import SellerForm from "@/views/SellerForm";
import SellerPage from "@/views/SellerPage";
import UserPage from "@/views/UserPage";

const routes = [
  {
    path: "/home",
    name: "Home",
    component: Home,
  },
  {
    path: "/signup/customer",
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
    props: true
  },
  {
    path: "/signup/seller",
    name: "SellerForm",
    component: SellerForm,
  },
  {
    path: "/seller/:id",
    name: "Seller",
    component: SellerPage,
  },
  {
    path: "/user",
    name: "User",
    component: UserPage,
  },
    {
    path: "/payment",
    name: "PaymentForm",
    component: PaymentForm,
  },

  {
    path: "/login",
    name: "LogIn",
    component: () => import("@/views/LogIn"),
  },
  {
    path: "/signup",
    name: "SignUp",
    component: () => import("@/views/SignUp"),
  },
];

export const router = createRouter({
  history: createWebHashHistory(),
  routes,
});
