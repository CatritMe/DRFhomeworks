import stripe
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(product):
    """Создает продукт в страйпе"""
    lesson = product.lesson
    course = product.course
    if course is None:
        return stripe.Product.create(name="Lesson")
    if lesson is None:
        return stripe.Product.create(name="Course")


def create_stripe_price(amount, product):
    """Создает цену в страйпе"""
    return stripe.Price.create(
        currency="rub",
        unit_amount=amount * 100,
        product=product.get("id"),
    )


def create_stripe_session(price):
    """Создает сессию на оплату в страйпе"""
    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        line_items=[{"price": price.get('id'), "quantity": 1}],
        mode="payment",
    )
    return session.get('id'), session.get('url')
