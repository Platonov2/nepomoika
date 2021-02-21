/**
 * Класс товара.
 */
export default interface Product {

    /**
     * Все поля являются отображением получаемой с бэкенда модели класса Product.
     */
    productId: number;
    categoryId: number;
    price: number;
    name: string;
}
