import { createRouter, createWebHashHistory } from "vue-router";
import Home from "@/views/Home";
import CustomerForm from "@/views/CustomerForm";
import PaymentForm from "@/views/PaymentForm.vue";
import ProductForm from "@/views/ProductForm";
import ProductDetailedPage from "@/views/ProductDetailedPage.vue";
import SellerForm from "@/views/SellerForm";
import SellerPage from "@/views/SellerPage";
import UserPage from "@/views/UserPage";
import Invoice from "@/views/Invoice.vue";
import PurchaseHistory from "@/views/PurchaseHistory.vue";

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
    component: ProductDetailedPage,
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
    path: "/invoices",
    name: "Invoice",
    component: Invoice,
  },

  {
    path: "/purchases",
    name: "PurchaseHistory",
    component: PurchaseHistory,
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
