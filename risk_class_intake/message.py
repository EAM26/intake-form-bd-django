class Message:
    @staticmethod
    def get_body(
            name, city, date, requesting_party, risk_class, email,
            organizational,
            constructional, compartment, carryaway, electronic, shield, alarm,
            verification, reaction, customization, partial_security, frequency,
            item_names, item_values, item_attractiveness
    ):
        # Base details
        message = (
            f"A new intake form was submitted\n"
            f"NAME: {name}\n"
            f"CITY: {city}\n"
            f"DATE: {date}\n"
            f"REQUESTING PARTY: {requesting_party}\n"
            f"RISK CLASS: {risk_class}\n"
            f"EMAIL: {email}\n"
            f"ORGANIZATIONAL: {organizational}\n"
            f"CONSTRUCTIONAL: {constructional}\n"
            f"COMPARTMENT: {compartment}\n"
            f"CARRYAWAY: {carryaway}\n"
            f"ELECTRONIC: {electronic}\n"
            f"SHIELD: {shield}\n"
            f"ALARM: {alarm}\n"
            f"VERIFICATION: {verification}\n"
            f"REACTION: {reaction}\n"
            f"CUSTOMIZATION: {customization}\n"
            f"PARTIAL SECURITY: {partial_security}\n"
            f"FREQUENCY: {frequency}\n"
            f"\nITEMS:\n"
        )

        # Add item details
        for name, value, attractiveness in zip(item_names, item_values,
                                               item_attractiveness):
            message += f"{name} - {value} - {attractiveness}\n"

        return message
